import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from postprocessing import *
from simulations import simulations
from scipy.stats import linregress
from matplotlib.colors import ListedColormap
from natsort import natsorted


class data_constructor(object):
    
    def __init__(self):
        self.sim = simulations()
        self.show_plot = False

    def all(self):
        self.reference_model()
        self.timestep_var()
        self.courant_var()
        self.delta_x_var()
        self.delta_z_var()

    def reference_model(self):
        simruns = self.sim.reference_model.items()
        self._produce_data(simruns)

    def courant_var(self):
        simruns = self.sim.courant_numbers.items()
        self._produce_data(simruns)

    def timestep_var(self):
        simruns = self.sim.timestepsize.items()
        self._produce_data(simruns)
    
    def delta_x_var(self):
        simruns = self.sim.delta_x.items()
        self._produce_data(simruns)

    def delta_z_var(self):
        simruns = self.sim.delta_z.items()
        self._produce_data(simruns)

    def _produce_data(self, simruns):
        for k,v in simruns:
            data = dataset(*v.values())
            data.plot_salinity_time(store_data=True)
            data.plot_salinity_time2(store_data=True)
        
        if not self.show_plot: 
            plt.close('all')

def get_dispersion_data(group=None):
    with pd.HDFStore('stored_data.hdf5','a') as store:
        if group:
            dfs = [(store.select(s),store.get_storer(s).attrs.metadata) for s in store if s.startswith((f'/dispersion/{group}', '/dispersion/Reference model'))]
            return natsorted(dfs, key=lambda k: k[1].get('string_id'))
        else:
            dfs = [(store.select(s),store.get_storer(s).attrs.metadata) for s in store if s.startswith('/dispersion')]
            return natsorted(dfs, key=lambda k: k[1].get('string_id'))


def plot_single_cell_salinities(x='mid', n=6, condition=None, parameter='courant'):
    # Get correct x location
    if x == 'mid':
        c = 1
        depth = 4.5
        xloc = 5000
    if x == 'low':
        c = 0
        depth = 2.5
        xloc = 2500
    if x == 'high':
        c = 2
        depth = 6.5
        xloc = 7500
        
    if parameter == 'courant':
        group = 'Max. Courant'
        exclusion_strings = ('0.2', '0.3', '0.5', '0.6', '0.8', '0.9','1.1','1.2', '1.3','1.4', '1.5', '1.7', '1.8', '1.9')
        ref_model = 'Courant'

    if parameter == 'time':
        group = 'Time step size'
        exclusion_strings = ('5s', ' 1s', '20s', '30s', '40s', '60s', '70s', '80s', '90s', '120s', '140s', '160s', '180s', '300s','350s', '400s','500s', '1000s')
        ref_model = 'Courant'

    if parameter == 'delta_x':
        group = 'Resolution x-direction'
        ref_model = 'Δx'
        exclusion_strings = (' 5m', ' 10m', '400m', '200m', '50m', '36.5m', '25m')

    if parameter == 'delta_z':
        group = 'Resolution z-direction'
        ref_model = 'Δx'
        exclusion_strings = ('Δz = 0.5m', 'Δz = 0.43m', 'Δz = 0.37m', 'Δz = 0.3m','Δz = 0.22m')

    # get data from hdf5 file
    dfs = get_dispersion_data(group=group)

    # initiate plots
    fig, ax = plt.subplots(2,1)
    fig.suptitle(f'Salinity over time for a single cell, at a depth of {depth} at x ≈ {xloc} - absolute values and differences relative to reference model')

    ax[0].set_title('Absolute salinity values')
    ax[1].set_title('Salinity differences with reference model')

    # Plot regular data
    labels = []
    for i,(df,meta) in enumerate(dfs):
        name = meta.get('string_id')
        if name.startswith(f'Reference model'):
            if name.startswith(f'Reference model - {ref_model}'):
                ref = df
                ls = '--'
                if parameter == 'delta_z':
                    name = 'Reference model - Δz = 1m'

                if parameter == 'time':
                    name = 'Reference model - Δt = auto'

            else:
                continue
        elif name.endswith(exclusion_strings):
            continue
        else:
            ls = '-'

        df.index = df.index.map(lambda t: (datetime.datetime.strptime(t, '%H:%M') - datetime.datetime.strptime(df.index[0], '%H:%M')).total_seconds())
        p = df.iloc[:,c].plot(ax=ax[0], ls=ls)
        labels.append(name)

    ax[0].legend(labels)
    ax[0].grid()
    ax[0].set_xlabel('Time [s]')
    ax[0].set_ylabel('Salinity [ppt]')
    
    # Plot difference with reference model
    labels = []
    for j,(df,meta) in enumerate(dfs):
        name = meta.get('string_id')
        if name.startswith(f'Reference model') or name.endswith(exclusion_strings):
            if name.startswith(f'Reference model - {ref_model}'):
                ref = df
                ls = '--'
                if parameter == 'delta_z':
                    name = 'Reference model - Δz = 1m'

                if parameter == 'time':
                    name = 'Reference model - Δt = auto'
            else:
                continue
        else:
            ls = '-'

        df[f'diff{x}'] = df.iloc[:,c] - ref.iloc[:,c]
        p = df[f'diff{x}'].plot(ax=ax[1], ls=ls)
        labels.append(name)
    
    ax[1].legend(labels)
    ax[1].grid()
    ax[1].set_xlabel('Time [s]')
    ax[1].set_ylabel('Salinity difference [ppt]')


def plot_diffusion_data():
    fig,ax = plt.subplots(2,2, sharex=True, constrained_layout=True, gridspec_kw={'height_ratios':[2,1]})
    exclusion_strings = ('120s','140s','160s', '180s', '300s','350s', '400s','500s', '1000s', 'Δx = 5m', 'Δx = 10m','Δz = 0.5m', 'Δz = 0.43m', 'Δz = 0.37m', 'Δz = 0.3m','Δz = 0.22m')
    with pd.HDFStore('stored_data.hdf5','a') as store:
        df = store.select('diffusion')

        unique = df.parameter.unique()
        idx = np.argwhere(unique == 'Reference model')
        params = np.delete(unique, idx)
        palette = dict(zip(params, sns.color_palette()))
        palette["Reference model"] = "k"

        df = df[~df.string_id.str.endswith(exclusion_strings)]
        ldf_ax = sns.scatterplot(x='ldf_courant', y='ldf_diff_rate', ax=ax[0,0], data=df, hue='parameter', palette=palette)
        hdf_ax = sns.scatterplot(x='hdf_courant', y='hdf_diff_rate', ax=ax[0,1], data=df, hue='parameter', palette=palette)
    
    for p in params:
        reg_data = df[df.parameter == p]
        ldf_a, ldf_b, ldf_r, ldf_p, ldf_stderr = linregress(reg_data.ldf_courant, reg_data.ldf_diff_rate)
        hdf_a, hdf_b, hdf_r, hdf_p, hdf_stderr = linregress(reg_data.hdf_courant, reg_data.hdf_diff_rate)
        ldf_x = np.linspace(reg_data.ldf_courant.min(),reg_data.ldf_courant.max(), 100)
        hdf_x = np.linspace(reg_data.hdf_courant.min(),reg_data.hdf_courant.max(), 100)
        
        r0 = ax[0,0].plot(ldf_x, ldf_a*ldf_x + ldf_b, label=f'R-squared: {round(ldf_r**2,2)}')
        r1 = ax[0,1].plot(hdf_x, hdf_a*hdf_x + hdf_b, label=f'R-squared: {round(hdf_r**2,2)}')

        res_ldf = reg_data.ldf_diff_rate - (ldf_a*reg_data.ldf_courant + ldf_b) 
        res_hdf = reg_data.hdf_diff_rate - (hdf_a*reg_data.hdf_courant + hdf_b)

        r2 = ax[1,0].scatter(reg_data.ldf_courant, res_ldf, label=f'{p} - residual error')
        r3 = ax[1,1].scatter(reg_data.hdf_courant, res_hdf, label=f'{p} - residual error')
                
    #ax.legend(labels=['Low density front', 'High density front'])

    ax[0,0].grid()
    ax[0,0].legend()
    ax[0,0].set_ylabel('Diffusion rate [-]')
    ax[0,0].set_xlabel('Courant number [-]')
    ax[0,0].set_title('Low density front diffusion rates vs. observed Courant numbers')
   
    ax[0,1].grid()
    ax[0,1].legend()
    ax[0,1].set_ylabel('Diffusion rate [-]')
    ax[0,1].set_xlabel('Courant number [-]')
    ax[0,1].set_title('High density front diffusion rates vs. observed Courant numbers')

    ax[1,0].grid()
    ax[1,0].legend()
    ax[1,0].set_ylabel('Residual error diffusion rate [-]')
    ax[1,0].set_xlabel('Courant number [-]')
    ax[1,0].set_title('Residuals of the LDF linear fit vs. observed Courant numbers')
    
    ax[1,1].grid()
    ax[1,1].legend()
    ax[1,1].set_ylabel('Residual error diffusion rate [-]')
    ax[1,1].set_xlabel('Courant number [-]')
    ax[1,1].set_title('Residuals of the HDF linear fit vs. observed Courant numbers')

class plotter():
    def __init__(self):
        pass

    def all(self):
        self.courant_disp()
        self.timestep_disp()
        self.delta_x_disp()
        self.delta_z_disp()
        self.statistics()
        self.diffusion()

    def courant_disp(self):
        plot_single_cell_salinities(parameter='courant', x='low')
        plot_single_cell_salinities(parameter='courant', x='mid')
        plot_single_cell_salinities(parameter='courant', x='high')

    def timestep_disp(self):
        plot_single_cell_salinities(parameter='time', x='low')
        plot_single_cell_salinities(parameter='time', x='mid')
        plot_single_cell_salinities(parameter='time', x='high')

    def delta_x_disp(self):
        plot_single_cell_salinities(parameter='delta_x', x='low')
        plot_single_cell_salinities(parameter='delta_x', x='mid')
        plot_single_cell_salinities(parameter='delta_x', x='high')

    def delta_z_disp(self):
        plot_single_cell_salinities(parameter='delta_z', x='low')
        plot_single_cell_salinities(parameter='delta_z', x='mid')
        plot_single_cell_salinities(parameter='delta_z', x='high')

    def diffusion(self):
        plot_diffusion_data()

    def statistics(self):
        gen_statistics()

def gen_statistics():
    dfs = get_dispersion_data()
    x_low = pd.DataFrame()
    x_mid = pd.DataFrame()
    x_high = pd.DataFrame()
    exclusion_strings = ('120s', '140s', '160s', '180s','300s','350s', '400s','500s', '1000s', 'Δx = 5m', 'Δx = 10m', 'Δx = 400m','Δz = 0.5m', 'Δz = 0.43m', 'Δz = 0.37m', 'Δz = 0.3m','Δz = 0.22m')


    for df,meta in dfs:
        name = meta.get('string_id')
        if name.startswith('Reference model - Courant'):
            df.index = df.index.map(lambda t: (datetime.datetime.strptime(t, '%H:%M') - datetime.datetime.strptime(df.index[0], '%H:%M')).total_seconds())
            ref_prim = df

        if name.startswith('Reference model - Δx'):
            df.index = df.index.map(lambda t: (datetime.datetime.strptime(t, '%H:%M') - datetime.datetime.strptime(df.index[0], '%H:%M')).total_seconds())
            ref_sec = df

        if name.startswith('Reference model - Δz'):
            df.index = df.index.map(lambda t: (datetime.datetime.strptime(t, '%H:%M') - datetime.datetime.strptime(df.index[0], '%H:%M')).total_seconds())
            ref_ter = df

    for df,meta in dfs:
        name = meta.get('string_id')
        if name.startswith('Reference'):
            continue

        if name.endswith(exclusion_strings):
            continue

        if name.startswith(('Max. Courant', 'Δt')):
            ref = ref_prim

        if name.startswith('Δx'):
            ref = ref_sec

        if name.startswith('Δz'):
            ref = ref_ter
        

        df.index = df.index.map(lambda t: (datetime.datetime.strptime(t, '%H:%M') - datetime.datetime.strptime(df.index[0], '%H:%M')).total_seconds())

        x_low[name] = df.iloc[:,0] - ref.iloc[:,0]
        x_mid[name] = df.iloc[:,1] - ref.iloc[:,1]
        x_high[name] = df.iloc[:,2] - ref.iloc[:,2]
   

    names = ['Max. Courant', 'Δt', 'Δx', 'Δz']
    x_low_var = pd.DataFrame()
    x_mid_var = pd.DataFrame()
    x_high_var = pd.DataFrame()

    for n in names:
        if name.startswith(('Max. Courant', 'Δt')):
            ref = ref_prim
            if name.startswith('Max. Courant'):
                coeff_var = 0.56343617
            if name.startswith('Δt'):
                coeff_var = 1.080583486

        if name.startswith('Δz'):
            coeff_var = 0.492913582
            ref = ref_ter

        if name.startswith('Δx'):
            coeff_var = 0.956364287
            ref = ref_sec

        x_low_var[n] = x_low[[c for c in x_low.columns if c.startswith(n)]].std(1) / coeff_var
        x_mid_var[n] = x_mid[[c for c in x_mid.columns if c.startswith(n)]].std(1) / coeff_var
        x_high_var[n] = x_high[[c for c in x_high.columns if c.startswith(n)]].std(1) / coeff_var
    
    
    fig, axes = plt.subplots(3,1)
    fig.suptitle('Standard deviation of the salinity difference with the reference model for the different parameter variations')
    fig.subplots_adjust(hspace=0.4)
    
    x_mid_var.plot(legend=True, ax=axes[0])
    x_low_var.plot(legend=True, ax=axes[1])
    x_high_var.plot(legend=True, ax=axes[2])

    axes[0].set_title('At location of initial disturbance (x=5000)')
    axes[0].set_xlabel('Time [s]')
    axes[0].set_ylabel('Standard deviation [ppt]')
    axes[0].minorticks_on()
    axes[0].grid(True, which='both')

    axes[1].set_title('Low density front (x=2500)')
    axes[1].set_xlabel('Time [s]')
    axes[1].set_ylabel('Standard deviation [ppt]')
    axes[1].minorticks_on()
    axes[1].grid(True, which='both')

    axes[2].set_title('High density front (x=7500)')
    axes[2].set_xlabel('Time [s]')
    axes[2].set_ylabel('Standard deviation [ppt]')
    axes[2].minorticks_on()
    axes[2].grid(True, which='both')

    x_low = x_low.reset_index().melt('time', var_name='parameter', value_name='data')
    x_mid = x_mid.reset_index().melt('time', var_name='parameter', value_name='data')
    x_high = x_high.reset_index().melt('time', var_name='parameter', value_name='data')

    x_low['parameter'] = x_low.parameter.map(lambda p: p.split(' = ')[0])
    x_mid['parameter'] = x_mid.parameter.map(lambda p: p.split(' = ')[0])
    x_high['parameter'] = x_high.parameter.map(lambda p: p.split(' = ')[0])
     
    ax1 = sns.relplot(x='time', y='data', hue='parameter',kind='line', ci='sd', data=x_low)
    ax1.ax.minorticks_on()
    ax1.ax.grid(True, which='both')

    ax2 = sns.relplot(x='time', y='data', hue='parameter',kind='line', ci='sd', data=x_mid)
    ax2.ax.minorticks_on()
    ax2.ax.grid(True, which='both')

    ax3 = sns.relplot(x='time', y='data', hue='parameter',kind='line', ci='sd', data=x_high)
    ax3.ax.minorticks_on()
    ax3.ax.grid(True, which='both')

    ax1.set(ylabel='Salinity difference [ppt]', xlabel='Time [s]', title='Salinity differences with respective reference model for different parameter variations at x=2500')
    ax2.set(ylabel='Salinity difference [ppt]', xlabel='Time [s]', title='Salinity differences with respective reference model for different parameter variations at x=5000')
    ax3.set(ylabel='Salinity difference [ppt]', xlabel='Time [s]', title='Salinity differences with respective reference model for different parameter variations at x=7500')


