# Results
## Modelling 
As a first exploration a few models were run with a single layer in the vertical direction. After some basic results were obtained the first results of experiments with 10 layers in the vertical direction were analyzed using Python based post-processing. Herafter consistently two output parameters averaged over the width were compared over time: the waterlevel and the salinity. During the modelling phase two sets of parameters were changed; Temperature and number of layers in the z-direction. The initial salinity difference was 10 ppt,the grid consisted of 100x3 cells and the simulation spanned 4 hours. The two performed variations are presented below along with general observations and conclusions regarding the reference model. Further settings and other results can be found in appendix \ref{appendix-modelling-results}.

### Old reference model results
#### Temperature variations
As to the salinity some observations can be made. 

- The frontal wavespeeds at both fronts are almost linear over time. This indicates an energy conserving approximation may be valid.
- The frontal wavespeed in the high density wave is lower than in the low density wave. This is probably because of the bed friction.
- At 6 degrees Celsius the model shows numerical diffusion characteristics for the low density wave. At higher temperatures it shows no direct numerical diffusion characteristics. However at 4 degrees celsius on a different run it shows no such numerical diffusion characteristics. It is unclear why simulation 1205-3 shows this behaviour.
- At 4 degrees Celsius the frontal wavespeeds are higher than at higher temperatures (10 and 15 degC). This can be explained through the formula that estimates the frontal wavespeed based on the density difference and the waterdepth: U = 0.5∙√(g'∙d). Where g'=g(ρ2-ρ1)/ρ2, given ρ1 < ρ2. [@Pietrzak1998]. If the density of water decreases the factor (ρ2-ρ1)/ρ2 will decrease as well, thus increasing the effect of the salinity difference. Now, because water has it's highest density at 4 degrees celsius, the effect of the density difference due to the salinity increases at higher or lower temperatures, meaning the reduced gravity will be smaller and thus the frontal wavespeed will be smaller. This explains that wave frontal speed will be at its maximum at 4 degrees celsius.
- At locations where internal waves may be formed the plot should be more detailed to draw conclusions. Also velocity profiles would be desirable. 

![Contour plot - width averaged salinity for T=10 degrees Celsius\label{contour-plot-1305-2}](./Width-averaged-salinity-contour-extremes-1305-2.png)

As to the waterlevel the following can be said:

- When the temperature is higher, in the first timestep, oscillations in the waterprofile can be seen in front of the disturbance, besides a large discontinuity around the center of the grid is observed. The fact that these oscillations are not observed at a temperature of 6 degC can be explained due to the relative effect the salinity difference has on the initial density difference, because this effect is smaller at lower temperatures due to a higher density of the water itself the disturbance is of a lower order than at higher temperature. These oscillations are could be a form of numerical dispersion and may be attributed to the hydrostatic assumption of the model, i.e. to compensate for the large vertical velocity gradient in the center of the grid at t=5min the model imposes a waterlevel difference (the large discontinuity). Subsequently to deal with this waterlevel difference in the middle of the grid, the approximation shows oscillations, i.e. in order to bridge the discontinuity in the waterlevel and approximate the original waterlevel at locations where the disturbance has not yet had any influence.
- Other oscillations are observed after the wavefronts (especially the high density wave) has passed. These oscillations could be a result of the artificial viscosity of the model, a process imposed to mimick energy loss due to heat transfer, this results in a transfer of kinetic energy in the form of waves. However, they could also be a result of the internal waves formed due to friction at the interface of the two density currents. Because in this mixing layer turbulence is likely to occur the model could show oscillations in the waterlevel to compensate for the vertical velocity gradients associated with turbulence.

![Waterlevel - Width averaged waterlevel over time for T=10 degrees Celsius\label{waterlevel-plot-1305-2}](./Width-averaged-waterdepth-1305-2.png')

Because the temperature difference has an indirect effect on the forcing it is desirable to keep this at a constant level and try out a range of different salinity deltas. With this reasoning a default temperature of 4 degrees Celsius should be sustained. A final check in 1305-4 where a background temperature of 0 degrees Celsius, shows similar results as obtained from 1305-2 where a temperature of 10 degrees Celsius was set. Given that the density of water at 0 degrees (9998.7 kg/m³) and 10 degrees (9997.5 kg/m³) are similar, this substantiates this similarity. Finally the results obtained in a situation with 4 degree Celsius is presented. 

![Contour plot - width averaged salinity for T=4 degrees Celsius\label{contour-plot-1305-5}](./Width-averaged-salinity-contour-extremes-1305-5.png)

#### Variations in number of layers in z-direction
As to the salinity some observations can be made:

- The frontal wave speed of the lower density current seems to increase increasing layers. The frontal wave speed of the high density current remains almost the same. A frontal wave speed for the low density front of 0.38 m/s, 0.39 m/s and 0.42 respectively for simulations with 20, 50 and 99 depth layers. It seems as if it will approximate the estimated value of 0.49 m/s. 

- Also fewer oscillations at the location where internal waves are expected are possibly observed. 

![Contour plot - width averaged salinity for #z-layers=99\label{contour-plot-1305-8}](./Width-averaged-salinity-contour-extremes-1305-8.png)

As to the waterlevel some observations can be made:

- The waterlevel seems across all levels seems similar except for the oscillations at locations where the front has already passed, and ofcourse the difference in wavespeed can be observed. In fact compared to the 10 layered model short oscillations seem to dissapear with 20, 50 and 99 layers. However these shorter oscillations seem to be replaced by a single larger oscillation near the end of the simulation (between t=2h and t=4h), increasingly large as the number of layers increase. This could be attributed to the gradual compensation of the waterlevel difference between the locations where the two wave fronts are situated, but it could also be a measure of the internal waves formed at the interface of the two density currents to compensate for the vertical velocity. This requires further investigation.  
- Small oscillations around a constant waterlevel difference across the first 3km of the grid, in each direction, at t=5min are similar across all simulations and indicate numerical dispersion to compensate for the discontinuity of the initial disturbance. 
- The waterlevel dfferences at the locations of each wave front are again expected to be caused by the vertical velocity gradients near the wavefronts for which the model compensates with a waterlevel rise, to fulfill the hydrostatic condition. 
- At a larger number of layers the absolute waterlevel difference across the first 3km of the grid, in each direction, seems to persist longer in the first 40min of the simulation. 

![Waterlevel - Width averaged waterlevel over time for #z-layers=99\label{waterlevel-plot-1305-8}](./Width-averaged-waterdepth-1305-8.png')

#### General observations
##### Physical observations
The following physical process characteristic for the lock-exchange experiment are observed during both the temperature variations and the variations in number of z-layers.

- The frontal wavespeeds at both fronts are almost linear over time. This indicates an energy conserving approximation may be valid.
- The frontal wavespeed in the high density wave is lower than in the low density wave. This is probably because of the bed friction.
- For the temperature variations the results indicate a temperature of 4 degrees gives the highest water density thus the highest frontal wavespeed. However simulating at a higher temperature could be more relevant, moreover the effect of the salinity difference is more noticable, this is taken into account in the determination of the reference model.
- For the variation of the number of layers in the vertical direction the frontal wavespeed increases a lot as the number of layers increase. It approaches a theoretical estimation as proposed by @Pietrzak1998.

##### Numerical observations
With respect to numerical phenomena the following is observed:

- Numerical dispersion is observed during all simulations at t=5min to deal with the initial disturbance in the waterlevel. This initial disturbance is originates from the model's hydrostatic condition and the large vertical velocity gradients at the start of the simulation.
- Numerical diffusion is possibly observed near the interface of the two density currents. In this mixing layer where turbulunce due to increased shear stresses is expected and clear oscillations are observed when the number of layers is 10. At a higher vertical resolution these short oscillations become a large oscillation with a single wavelenght stretching the grid. This transformation could be a result of the ratio between the horizontal and vertical resolution (1/1000 and 1/100 for 99 and 10 layers respectively) causing different modes in the approximation to be emphasized while trying to account for turbulence in the mising layer.
- The higher resolution, in simulations with more layers, cause more oscillations in the salinity contour lines to be visible near the front. These small oscillations are expected to be numerically diffused turbulence that may be expected at the progressing wavefronts.


#### Conclusions
The computation times were all within reasonable limits while the number of layers in the z-direction reached it's limit at 99. This is a positive result considering future variations in the spatial resolution. With respect to temperature also positive results are obtained that coincide with the expected physics, for this parameter a constant value of 4 degrees celsius can be reasonably determined. However to obtain better insight in what causes the observed phenomena and how these relate to the numerical accuracy of the model more information is required. To this end other plots that are within reach and could be interesting are listed below:

- A table with the extreme values and there order of error
- Courant liming cells in the vertical
- Velocity magnitudes and vertical velocity 
- 3D profiles instead of width averaged plots to get an idea of the numerical effects in the horizontal 
- Detailed plots for the middle of the grid and at locations both fronts to get a detailed view on how the model deals with internal waves and large disturbances respectively.


### Observations
The above results have to be largely summarized and observations of the plots below will be documented. This will give a full description of the reference model.

![Width averaged salinity for the reference model\label{contour-salinity-2605-1}]('./contourplot-2601-1.png')
![Single cell salinity for the reference model\label{sinle-cell-2605-1}]('./single-cell-salinity-2601-1.png')
![Single cell salinity for the reference model - all layers\label{single-cell-all-2605-1}]('./single-cell-salinity-all-layers-2601-1.png')
![Detailed plot of the front for the reference model\label{detailed-2605-1}]('./detailed-plot-2601-1.png')
![Depth maximized number of times a cell was courant limiting\label{courant-limiting-2605-1}]('./courant-limiting-2601-1.png')

### Final settings
The settings and conclusions related to the reference model are described.


## Simulations
Here the results per parameter variation will be presented. 

### Interval analysis
Here an interval analysis will be presented for parameters of the model that will be varied during the simulations. Based upon this a valid reasoning for the chosen parameter range is provided.

### Temporal varations
#### Courant number
![Single cell salinity over time for different courant numbers\label{single-cell-analysis-courant-x5050}]('./single-cell-analysis-courant-x5050.png')
![Single cell salinity over time for different courant numbers\label{single-cell-analysis-courant-x2250}]('./single-cell-analysis-courant-x2550.png')
![Single cell salinity over time for different courant numbers\label{single-cell-analysis-courant-x7650}]('./single-cell-analysis-courant-x7650.png')
![Diffusion table for different courant numbers\label{diffusion-table-courant}]('./table-diffusion-courant.png')


### Spatial variations
### Initial salinity
### Numerical variations

### Numerical evaluation criteria
Several numerical evaluation criteria, as explained in appendix \ref{appendix-numerics} and according to their relevance to a parameter, will be compared to the results.

## Sensitivity analyis
The sensitivity analysis based 
