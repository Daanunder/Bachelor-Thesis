import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import matplotlib.colors as colors
from scipy.optimize import curve_fit
import h5py

class dataset():
    def __init__(self, netcdf_file, run_id, string_id, sal_min, sal_max, depth,layers, delta_x, parameter):
        self.dataset_location = netcdf_file 
        self.dataset = xr.open_dataset(self.dataset_location)
        self.df_waterdepth = self.dataset.mesh2d_waterdepth.to_dataframe()
        self.df_salinity = self.dataset.mesh2d_sa1.to_dataframe()
        self.run_id = 'run_'+run_id
        self.string_id = string_id
        self.sal_min = sal_min
        self.sal_max = sal_max
        self.depth = depth
        self.courant_lim = self.dataset.mesh2d_Numlimdt.to_dataframe().groupby(['mesh2d_face_x']).max()['mesh2d_Numlimdt']
        self.ldf_courant = []
        self.hdf_courant = []
        self.layers=layers
        self.significance = 3
        self.time = self.df_salinity.index.unique(level='time')
        self.velocity_mag = self.dataset.mesh2d_ucmag.to_dataframe()
        self.velocity_x = self.dataset.mesh2d_ucx.to_dataframe()
        self.velocity_z = self.dataset.mesh2d_ucz.to_dataframe()
        self.timestep = self.dataset.timestep.to_dataframe()
        self.ldf_diffusion = []
        self.hdf_diffusion = []
        self.extremes = []
        self.data_file = 'stored_data.hdf5'
        self.delta_x = delta_x
        self.delta_t = np.round(self.timestep.mean()[0], 2)
        self.parameter = parameter
        self.max_obs_velocity = self.velocity_x['mesh2d_ucx'].max()
        self.max_velocity_z = self.velocity_z['mesh2d_ucz'].max()

    def theoretical_frontal_wavespeed(self):
        p1 = 1000+self.sal_min
        p2 = 1000+self.sal_max
        Y = min(p1/p2, p2/p1)
        g = 9.81
        gr = g*(1-Y)
        return 0.47*np.sqrt(gr*self.depth), 0.59*np.sqrt(gr*self.depth)

    def plot_waterdepth_time(self, n=1, save=False, fig_name='width_averaged_waterdepth'):
        '''
        Plots n number of equal time differenced plots of the waterdepth averaged over the width. The initial situation (t=0) the first timestep (t=Δt) and the last (t=tmax) times are always plotted. E.g. if n=4, the simulation was 4 hours and the timedelta 5min the plot will contain the following timesteps (t=0, t=5min, t=60min, t=120min, t=180min, t=240min). 
        ''' 
        #time = self.df_waterdepth.index.unique(level='time')
        time = self.time

        # plot initial situation
        t_delta = self.df_waterdepth.loc[time[0]].groupby('mesh2d_face_x').mean()
        name = time[0].strftime('t=%Hh:%Mm')
        t_delta.mesh2d_waterdepth.plot(label=name) 

        for t_idx in range(0, len(time), int(len(time)/n)):
            if t_idx == 0:
                t_idx=1
            name = time[t_idx].strftime('t=%Hh:%Mm')
            t_delta = self.df_waterdepth.loc[time[t_idx]].groupby('mesh2d_face_x').mean()
            t_delta.mesh2d_waterdepth.plot(label=name) 

       
        plt.title(f'Width averaged waterdepth - {self.run_id}')
        plt.xlabel('Position in canal [m]')
        plt.ylabel('Waterdepth [m]')
        plt.legend()
        plt.minorticks_on()
        plt.grid(True, which='both')

    def plot_salinity_time(self, n=4, save=False, fig_name='Width_averaged_salinity', heatmap=False, contour=True, extremes=True, fps_line=True, store_data=False, detailed_plots=False):
        # reset averages
        self.ldf_diffusion = []
        self.hdf_diffusion = []
        
        # Necessary to avoid 'reference before assignment' error
        fps_red = None
        fps_blue = None
        hdf_red = None
        ldf_blue = None

        #time = self.df_salinity.index.unique(level='time')
        time = self.time
        df = self.df_salinity.reset_index(level='mesh2d_nLayers')

        # Initiate subplots
        fig, axes = plt.subplots(n+2, 1, sharex=True, sharey=True)
        fig.subplots_adjust(hspace=0.7)

        # plot initial situation
        avg_sal = df.loc[time[0]].groupby(['mesh2d_face_x', 'mesh2d_nLayers']).mean()['mesh2d_sa1']
        avg_sal = avg_sal.reset_index() 
        piv = avg_sal.pivot_table(values='mesh2d_sa1', index='mesh2d_nLayers', columns='mesh2d_face_x')  # create grid

        if heatmap:
            hm = sns.heatmap(piv, ax=axes[0], cmap='plasma', cbar_kws={'label':'Salinity [ppt]'}, cbar_ax=fig.add_axes([.92, .2, .03, .3]))
            hm.invert_yaxis()
            plottype = 'Heatmap'

        if contour: 
            x,y=np.meshgrid(piv.columns,piv.index)
            axes[0].grid()
            cf = axes[0].contourf(x,y, piv.values)
            cp = axes[0].contour(x,y, piv.values, levels=[15, 16, 24, 25], colors='black')
            axes[0].clabel(cp, cp.levels, colors='black', fontsize=6)
            fig.colorbar(cf, cax=fig.add_axes([.92,.2,.03,.3]))
            plottype = 'Contourlines'

        if extremes:
            rdots=None
            bdots=None
            df_lows = avg_sal[round(avg_sal.mesh2d_sa1, self.significance) < 15].reset_index()
            if not df_lows.empty:
                bdots = axes[0].plot(df_lows.mesh2d_face_x, df_lows.mesh2d_nLayers, 'b*')
            df_highs = avg_sal[round(avg_sal.mesh2d_sa1, self.significance) > 25].reset_index()
            if not df_highs.empty:
                rdots = axes[0].plot(df_highs.mesh2d_face_x, df_highs.mesh2d_nLayers, 'r*')
           
            self.extremes = [df_lows, df_highs]


        name = time[0].strftime('t=%Hh:%Mm')
        axes[0].set_title(name)
        axes[0].get_yaxis().get_label().set_visible(False)
        axes[0].get_xaxis().get_label().set_visible(False)
        axes[0].set_yticks([0,self.layers-1])
        axes[0].set_yticklabels([str(self.depth), '0'])
        axes[0].minorticks_on()
        axes[0].grid(True, which='both')
        

        i = 0
        for t_idx in range(0, len(time), int(len(time)/n)):
            i+=1

            if i == 3:
                self.observation_time = time[t_idx]

            # Plot the situation after one timestep
            if t_idx == 0:
                t_idx=1

            avg_sal = df.loc[time[t_idx]].groupby(['mesh2d_face_x', 'mesh2d_nLayers']).mean()
            if avg_sal.dropna().empty:
                time_name = time[t_idx].strftime('t=%Hh:%Mm')
                axes[i].set_title(f'No data found for {time_name}')
                continue
            avg_sal = avg_sal.reset_index() 
            piv = avg_sal.pivot_table(values='mesh2d_sa1', index='mesh2d_nLayers', columns='mesh2d_face_x')  # create 2d meshgrid with values
            
            if heatmap:
                hm = sns.heatmap(piv, cmap='plasma', ax=axes[i], cbar=False)
                #hm.invert_yaxis()

            if contour:
                x,y=np.meshgrid(piv.columns,piv.index)
                cf = axes[i].contourf(x,y, piv.values)
                cp = axes[i].contour(x,y, piv.values, levels=[15, 16, 24, 25], colors='black')
                axes[i].clabel(cp, cp.levels, colors='black', fontsize=6)

            if extremes:
                df_lows = avg_sal[round(avg_sal.mesh2d_sa1,self.significance) < 15].reset_index()
                if not df_lows.empty:
                    bdots = axes[i].plot(df_lows.mesh2d_face_x, df_lows.mesh2d_nLayers, 'b*')
                    
                df_highs = avg_sal[round(avg_sal.mesh2d_sa1,self.significance) > 25].reset_index()
                if not df_highs.empty:
                    rdots = axes[i].plot(df_highs.mesh2d_face_x, df_highs.mesh2d_nLayers, 'r*')

                self.extremes.append([df_lows, df_highs])
            
            if fps_line:
                # Plot analytical front locations
                fps_high, fps_low = self.theoretical_frontal_wavespeed()
                time_delta = (time[t_idx] - time[0]).total_seconds()
                xhigh = 5100+fps_high*time_delta 
                xlow = 5100-fps_low*time_delta

                if xhigh < 10000 and t_idx > 1:
                    fps_red = axes[i].axvline(xhigh, color='r', lw=2)
                if xlow > 0 and t_idx > 1:
                    fps_blue = axes[i].axvline(xlow, color='b', lw=2)
               
                # Plot actual front locations
                sal_diff = df.loc[time[t_idx]].groupby(['mesh2d_face_x', 'mesh2d_nLayers']).mean()
                sal_diff = sal_diff.reset_index(level='mesh2d_nLayers').diff(periods=self.layers)

                hdf_location = max(sal_diff.index[sal_diff['mesh2d_sa1'].abs() > 1/self.delta_x]) - 2*self.delta_x 
                ldf_location = min(sal_diff.index[sal_diff['mesh2d_sa1'].abs() > 1/self.delta_x])
                
                if t_idx > 1 and axes[i] not in axes[-2:]:
                    hdf_red = axes[i].axvline(hdf_location, color='r', ls='--', lw=2)
                    ldf_blue = axes[i].axvline(ldf_location, color='b', ls='--', lw=2)
               
                diff_name = ''
                if axes[i] not in axes[-2:] and t_idx > 1:
                    ldf_factor = (abs(5100-ldf_location)/time_delta) / fps_low
                    hdf_factor = (abs(5100-hdf_location)/time_delta) / fps_high
                    
                    t_step = self.timestep.loc[time[t_idx]]['timestep']
                    velocity = self.velocity_x.loc[time[t_idx]]

                    ldf_flow_velocity = velocity[(velocity.mesh2d_face_x >= ldf_location) & (velocity.mesh2d_face_x <= ldf_location + 200)]['mesh2d_ucx'].min()
                    hdf_flow_velocity = velocity[(velocity.mesh2d_face_x >= hdf_location - 200) & (velocity.mesh2d_face_x <= hdf_location)]['mesh2d_ucx'].max()

                    ldf_courant = ldf_flow_velocity * t_step / self.delta_x 
                    hdf_courant = hdf_flow_velocity * t_step / self.delta_x

                    self.ldf_courant.append(ldf_courant)
                    self.hdf_courant.append(hdf_courant)
                    self.ldf_diffusion.append(ldf_factor)
                    self.hdf_diffusion.append(hdf_factor)
                    diffratehdf = round(hdf_factor,2)
                    diffrateldf = round(ldf_factor,2)
                    diff_name = f'- HDF diffusion rate: {diffratehdf} - LDF diffusion rate: {diffrateldf}'


            time_name = time[t_idx].strftime('t=%Hh:%Mm')
            axes[i].set_title(f'{time_name} {diff_name}')
            axes[i].set_yticks([0,self.layers-1])
            axes[i].set_yticklabels([str(self.depth), '0'])
            axes[i].minorticks_on()
            axes[i].grid(True, which='both')
            
            if i != n+1:
                axes[i].get_xaxis().get_label().set_visible(False)
            if i != round(len(axes)/2):
                axes[i].get_yaxis().get_label().set_visible(False)

        
        if detailed_plots:
            print('Plotting details')
            # Initiate second figure
            fig2, axes2 = plt.subplots(2,2)
            fig2.subplots_adjust(hspace=0.3)
            time_name = self.observation_time.strftime('t=%Hh:%Mm')
            fig2.suptitle(f'Detail plot of high- and low density fronts at {time_name} - {self.string_id}')


            avg_sal = df.loc[self.observation_time].groupby(['mesh2d_face_x', 'mesh2d_nLayers']).mean()
            avg_sal = avg_sal.reset_index() 
            piv = avg_sal.pivot_table(values='mesh2d_sa1', index='mesh2d_nLayers', columns='mesh2d_face_x')  # create 2d meshgrid with values

            # Get actual front locations
            sal_diff = df.loc[self.observation_time].groupby(['mesh2d_face_x', 'mesh2d_nLayers']).mean()
            sal_diff = sal_diff.reset_index(level='mesh2d_nLayers').diff()
            hdf_location = max(sal_diff.index[sal_diff['mesh2d_sa1'].abs() > 1/self.delta_x]) - 2*self.delta_x
            ldf_location = min(sal_diff.index[sal_diff['mesh2d_sa1'].abs() > 1/self.delta_x])
            
            # Create plots with xlim 
            x,y=np.meshgrid(piv.columns,piv.index)
            
            names = ['Low density front - salinity',  'Low density front - courant number', 'High density front - salinity', 'High density front - courant number']
            limits = [[1000,1000], [1000,1000], [1000,1000], [1000,1000]]
            idxs = [0,0],[1,0],[0,1],[1,1]

            for j,name in enumerate(names):
                if j in [0,1]:
                    loc = ldf_location
                    color = 'b'
                else:
                    loc = hdf_location
                    color = 'r'
                
                r,c = idxs[j]
                xmin = loc - limits[j][0]
                xmax = loc + limits[j][1]

                if r == 0:
                    cf = axes2[r,c].contourf(x,y, piv.values)
                    cp = axes2[r,c].contour(x,y, piv.values, levels=[15, 16, 24, 25], colors='black')
                    axes2[r,c].clabel(cp, cp.levels, colors='black', fontsize=6)
                    axes2[r,c].set_xlim(max(xmin,0), min(xmax, 10000))

                    axes2[r,c].axvline(loc, color=color, ls='--')

                    axes2[r,c].set_title(name)
                    axes2[r,c].set_yticks([0,self.layers-1])
                    axes2[r,c].set_yticklabels([str(self.depth), '0'])
                    axes2[r,c].set_xlabel('Position [m]')
                    axes2[r,c].set_ylabel('Depth [m]')

                else:
                    t_step = self.timestep.loc[self.observation_time]['timestep']
                    max_velocity = self.velocity_x.loc[self.observation_time].groupby('mesh2d_face_x').max()['mesh2d_ucx']
                    max_courant = max_velocity * t_step / self.delta_x
                    max_courant.plot(ax=axes2[r,c])
                    axes2[r,c].set_xlim(max(xmin,0), min(xmax, 10000))

                    axes2[r,c].set_title(name)
                    axes2[r,c].grid()
                    axes2[r,c].set_xlabel('Position [m]')
                    axes2[r,c].set_ylabel('Courant number')

        # Plot legend if applicable
        if extremes or fps_line:
            handles=[]
            labels=[]
            if rdots:
                handles.append(rdots[0])
                labels.append(f'Significant values > {self.sal_max:.3f}ppt')

            if bdots: 
                handles.append(bdots[0])
                labels.append(f'Significant values < {self.sal_min:.3f}ppt')
            
            if fps_red:
                handles.append(fps_red)
                labels.append(f'Analytically defined location of the high density front')
            
            if fps_blue:
                handles.append(fps_blue)
                labels.append(f'Analytically defined location of the low density front')

            if hdf_red:
                handles.append(hdf_red)
                labels.append(f'Measured location of the high density front')

            if ldf_blue:
                handles.append(ldf_blue)
                labels.append(f'Measured location of the low density front')

            fig.legend(handles=handles, labels=labels, loc='center right', bbox_to_anchor=(0.7, 0.5, 0.3 , 0.5), framealpha=1)


        self.ldf_courant_mean = abs(np.mean(self.ldf_courant))
        self.hdf_courant_mean = abs(np.mean(self.hdf_courant))
        ldf_diff_rate = abs(np.mean(self.ldf_diffusion))
        hdf_diff_rate = abs(np.mean(self.hdf_diffusion))

        fig.suptitle(f'Width averaged salinity - {self.string_id} - Avg. LDF diffusion rate: {round(ldf_diff_rate,2)} - Avg. HDF diffusion rate: {round(hdf_diff_rate,3)}')
        axes[-1].set_xlabel('Position in canal [m]')
        axes[round(len(axes)/2)].set_ylabel('Depth [m]')
        fig.tight_layout(rect=[.1,.1,.7,.7])
        

        if store_data:
            with pd.HDFStore(self.data_file, 'a') as store:
                fps_high, fps_low = self.theoretical_frontal_wavespeed()
                keys = ['index', 'fps_low', 'fps_high', 'ldf_diff_rate', 'hdf_diff_rate', 'ldf_courant', 'hdf_courant', 'max_courant_lim', 'max_velocity_x', 'max_velocity_z', 'string_id', 'parameter'] 
                values = [self.run_id, round(fps_low,self.significance), round(fps_high,self.significance), ldf_diff_rate, hdf_diff_rate, self.ldf_courant_mean, self.hdf_courant_mean, self.courant_lim.max(), self.max_obs_velocity, self.max_velocity_z, self.string_id, self.parameter]
                diffusion_data = dict(zip(keys,values))

                print(f'\n ------- \n Writing diffusion data of {self.run_id}')
                print(f'{diffusion_data}')
                store['diffusion'] = store.get('diffusion').append(pd.DataFrame(diffusion_data, index=[0])).drop_duplicates(subset='index', keep='last')


## MISC
    def _hyperbola(self,x,a,b,c,d,e):
        return (a*np.e**(b*(x - 5000)/10000) + c*np.e**(d*(x-5000))) + e

    def fit_hyp(self, t_idx, low=19, high=21, significance=None):
        if significance == None:
            significance = self.significance

        df = self.df_salinity.reset_index(level='mesh2d_nLayers')
        time = self.time
        sal = df.loc[time[t_idx]].groupby(['mesh2d_face_x', 'mesh2d_nLayers']).mean()['mesh2d_sa1']
        condition = np.all([round(sal,significance) > low, round(sal,significance) < high], axis=0)
        data = sal[condition].reset_index(level='mesh2d_nLayers')
        data.mesh2d_nLayers = data.mesh2d_nLayers * 10/self.layers

        a,b,c,d,e = curve_fit(self._hyperbola, data.index, data.mesh2d_nLayers, [10000,1,10001,1])[0]

        x = np.linspace(min(data.index)-100,max(data.index)+250,1000)
        y = self._hyperbola(x,a,b,c,d,e)
        #ytop = 10
        #ybot = 0
#
        #top_idx = np.argwhere(np.diff(np.sign(y - ytop)))
        #bot_idx = np.argwhere(np.diff(np.sign(y - ybot)))

        #print(top_idx, bot_idx)

        #plt.axvline(x[top_idx])
        #plt.axhline(x[bot_idx])

        plt.plot(data.index, data.mesh2d_nLayers, 'r*')
        plt.plot(x,y)

    def plot_salinity_time2(self, n=2, xdiff=2500, store_data=False):
        # Plot
        fig, axes = plt.subplots(3,1)
        plt.subplots_adjust(hspace=0.7)
        plt.suptitle(f'Salinity over time for a single cell - {self.string_id}')

        # Data
        df = self.df_salinity.reset_index().groupby(['time', 'mesh2d_nLayers', 'mesh2d_face_x']).mean()
        df = df.reset_index(level=['mesh2d_nLayers', 'mesh2d_face_x'])
        #xvals = np.sort(np.unique(np.arange(round(10000./(n+1), -2), 10000., round(10000./(n+1), -2))))+50
        xvals = np.round(np.array([5000 - xdiff, 5000, 5000+xdiff]) / self.delta_x)*self.delta_x + self.delta_x/2
        #layers = np.sort(np.unique([self.layers-1, 0, round(self.layers/2), round(self.layers/4), round(self.layers/3), round(self.layers*2/3), round(self.layers*3/4)]))
        layers = range(self.layers)
        
        # Initiate data storage
        dispersion_data = pd.DataFrame()

        for i,x in enumerate(xvals):
            sal = df[df.mesh2d_face_x == x]
            sal.index = sal.index.map(lambda t: t.time().strftime('%H:%M'))

            delta_z = 10/self.layers
            for l in layers:
                cell = sal[sal.mesh2d_nLayers == l]['mesh2d_sa1'] 
                p = axes[i].plot(cell.index, cell.values, label=f'Depth {round((self.layers-l)/self.layers * 10 - 0.5*delta_z, 1)}m')
                if i == 0:
                    max_disp_depth = round(round(3.5/delta_z) * delta_z - 0.5*delta_z,2)
                elif i == 2:
                    max_disp_depth = round(round(7.5/delta_z) * delta_z - 0.5*delta_z,2)
                else:
                    max_disp_depth = round(round(4.5/delta_z) * delta_z - 0.5*delta_z,2)

                if store_data and round((self.layers-l)/self.layers * 10 - 0.5*delta_z, 2) == max_disp_depth:
                    dispersion_data[x] = cell
                    

            #axes[i].minorticks_on()
            #axes[i].grid(True, which='both')
            axes[i].grid(which='major', color='black')
            if (df.index.unique()[1] - df.index.unique()[0]).total_seconds() < 5*60:
                axes[i].set_xticks(np.arange(0,len(sal.index.unique()),2))
                axes[i].set_xticklabels(sal.index.unique()[np.arange(0,len(sal.index.unique()),2)], rotation=45)
            else:
                axes[i].set_xticklabels(sal.index.unique(), rotation=45)
            axes[i].set_title(f'Location x: {x}m')
            axes[i].legend(framealpha=1)


        if store_data:
            print(f'\n ------- \n Writing dispersion of {self.run_id}')
            print(f'{dispersion_data}')
            with pd.HDFStore(self.data_file, 'a') as store:
                store[f'/dispersion/{self.parameter}/{self.run_id}'] = dispersion_data

                metadata = {'string_id':self.string_id, 'max_velocity':self.max_obs_velocity}
                store.get_storer(f'/dispersion/{self.parameter}/{self.run_id}').attrs.metadata = metadata

    
        fig.text(0.5, 0.04, 'Time [H:M]', ha='center')
        fig.text(0.04, 0.5, 'Salinity [ppt]', va='center', rotation='vertical')

    def plot_width_diff(self, df=None, n=4):
        if isinstance(df, type(None)):
            df = self.df_salinity

        data_col = [c for c in df.columns if c not in ['mesh2d_face_x', 'mesh2d_face_y']][0]
        df = df.rename(columns={data_col:'data_col'})

        time = self.time
            
        border_coord = df.mesh2d_face_y.unique()[0]
        center_coord = df.mesh2d_face_y.unique()[round(len(df.mesh2d_face_y.unique())/2)-1]
        diff = df[df.mesh2d_face_y == border_coord]['data_col'].values - df[df.mesh2d_face_y == center_coord]['data_col'].values

        if round(sum(abs(diff)),self.significance) == 0:
            print('There was no width dependency found in the data')
        else:
            return diff

    def plot_courant_numbers(self, n=4, limiting=False):
        if limiting:
            df = self.courant_lim
            df.plot.bar()
            plt.title(f'Number of times a cell was Courant limiting - {self.string_id}')
            plt.xlabel('Position [m]')

        else:
            time = self.time
            fig3, axes3 = plt.subplots()
            for t_idx in range(0, len(time), int(len(time)/n)):
                if t_idx == 0:
                    t_idx = 1
                t_step = self.timestep.loc[time[t_idx]]['timestep']
                max_velocity = self.velocity_x.loc[time[t_idx]].abs().groupby('mesh2d_face_x').max()['mesh2d_ucx']
                max_courant = max_velocity * t_step / self.delta_x

                name = time[t_idx].strftime('t=%Hh:%Mm')
                max_courant.plot(ax=axes3, label=name)

            axes3.grid()
            axes3.set_xlabel('Position [m]')
            axes3.set_ylabel('Courant number')
            axes3.legend()
            fig3.suptitle(f'Depth maximized Courant number over time - {self.string_id} - Δx: {self.delta_x}m - Δt: automatic -  Δt-average: {self.delta_t}s')

         




