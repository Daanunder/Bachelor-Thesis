# Method
To support answers to the research questions with data and reasonable arguments and thus finally obtain an indication and quantification of the numerical dispersion and -diffusion produced by D-Flow FM the following research method is presented.

The method is split in three phases: modelling, simulation, analysis, which respectively comprise the modelling and describing of the frame of reference, running simulations over a range of values per parameter and analyzing the results using a sensitiviy analysis and appropriate indicator parameters. Herafter the produced results can be discussed and possibly conclusions with respect to the to the research questions can be drawn.

## Reference model
During the modelling phase one determines a reference model through modelling large ranges of desirably constant parameters. Based on a qualitative analysis of these results the model settings and parameters that will remain constant throughout the further research are reasonably defined.

First the terms and settings found in the basic D-Flow FM model are explored. In this reference model the observed numerical dispersion and -diffusion should be of an acceptable range and more importantly subject to little change. In the initial reference model a basic setup of the boundary conditions, the width, lenght and depth of the model and timescale of the simulation are determined. This takes a few iterations and requires basic post processing of the results to asses the characteristic variables of the different simulations, in this case the temperature and number of layers in the vertical direction are considerd. Through the results presented in this report it becomes clear which settings give minimal numerical diffusion and dispersion.

In order to provide a solid basis for the sensitivity analysis the reference model has to be sufficiently robust to enable all parameters to be explored. Besides after every parameter variation constant value for this parameter should be logically determined. To ensure a working model first most default settings are used to set up the lock-exchange model. In this model the following parameters are thus defined; general settings such as working directory, model name etc. The basic geometry including lenght, width and depth. Basic physics such as water density, gravity acceleration etc. Boundary conditions being closed free-slip boundaries for either velocity or discharge. A computational grid with n- and m-number of cells in x- and y-direction respectively. And finally if desired location specific monitoring points with a higher frequency of output can be determined to reduce the memory load of the model. 

With respect to post-processing two parameters are evaluated; the width averaged waterlevel over time and the width averaged salinity over time. These state variables indicate numerical errors and enable classification of the observed error. For the salinity profiles points where they either have an extreme (physically unrealistic) value are highlighted and locations where characteristic values of the solution can be expected are inspected in more detail.

After reasonable accuracy and stability of the simulation is ensured the initial reference model is thus defined, although some final aspects of the model may be refined. Possibly more realistic physical properties, boundary conditions, a more relevant geometry or specifics of the flow model such as bed friction can be be set based on the qualitative analysis of the produced results. However, most of these are expected to be left at their default values and their are otherwise clearly substantiated with relevant arguments.

## Simulations
In order to generate the data required for the sensitivity analysis a number of simulations have to be performed. By varying the different parameters **the characteristic variables, defined as the frontal wavespeed, the thickness of the mixing layer and the waterlevel,** the associated numerical errors can be computed. Because this is done over a realistic and relevant range of values numerical diffusion and -dispersion errors produced by D-Flow FM can be quantified and accordingly conclusions based on flow related- and numerical indicators may be drawn.

### Interval analysis
To reasonably define the ranges for each parameter over which it will be varied an interval analysis is performed. This analysis will provide insight in what results come from different ranges of parameters and how applicable certain combinations of ranges are. Moreover it will provide insight in how many experiments have to be run and what values per parameter may be expected. **SOURCE AND FURTHER METHOD**

### Parameter variations
Based on variation in temperature and number of layers in the z-direction the model's response to some basic parameters is explored. Based upon these observations an initial reference model for the temporal variations is determined. For the parameter variations the sequential order matters as it is desirable to have a constant timestep for all variations and therefore to have investigated the effect of the Courant number in combination with D-Flow FM's automatic time step setting before setting this constant timestep. Lastly when the temporal and spatial variations are finalized a reference model can be set up for the variation of miscellaneous numerical parameters such as type of numerical scheme and limiter or entrainment and friction types.

After simulations with a varying Courant number, while using the automatic time step setting in D-Flow FM (see appendix \ref{appendix-dflow}), the first results are examined and compared to the reference model. Because the Courant number plays an important role in computational fluid dynamics it serves as an important measure in the subsequent variations. Herafter the timestep is set constant over the simulation and it's size is varied, which gives the variation of the time step size parameter. By the means of these results a constant time step size for the next parameter variations will be chosen. Herewith a constant reference model for the spatial variations is thus obtained. 

Next, naturally, the spatial resolution is varied and examined. Possibly because of the third order factor of space monitoring points may be desirable in order to maintain realistic computation times. These monitoring points have to be set up at logically sound locations within the reference model and will give a high resolution insight in the development of characteristic variables at specific locations over time.  Although the number of layers is prematurely examined in the reference model both Δx and Δz are varied. This is initially done for the default rectangular shaped meshgrid and later verified for different types of meshgrid, including triangles, quids, pentagons and hexagons. 

Finally other parameters such as the ones listed below can be varied and examined:

* Viscosity
* Bed friction
* Entrainment (mixing terms)
* Advection scheme
* Solver parameters 

For the experiments to be able to run the simulation procedure based on the reference model and the post-processing is automated as much as possible using Python. These scripts can be found in appendix \ref{appendix-python}. 


## Data analysis
The data analysis consists of a qualitative analysis of the results and accordingly a just quantification of the observed errors in order for the errors to be used in the sensitivity analysis. This is done, firstly, by plotting the Courant numbers at the low density front (LDF) and the high density front (HDF) versus the diffusion rates of these fronts, defined as the observed propagation speed of the front divided by the analytically defined propagation speed of the front [@Pietrzak1998]. Secondly, by looking at the salinity of a single cell over time at three different locations and at different depths, in order to observe the effect of both the fully developed fronts (travelling in opposite directions) and to get insight in what happens at the initial disturbance.

**During the qualitative analysis the results of all the post processing of the different performed experiments are analyzed and a relation between the sensitiviy of the observed numerical errors to the change in certain parameters are sought for, either physically or numerically. 

In order to correctly quantify the observed errors it will be determined what indicator parameters are of significance and what numerical conditions are applicable. Herafter a sensitivity analysis is performed, where the sensitivity of a parameter S(P) is defined as the relative change of a state variable per change of this parameter: S = (δx/x)/(δP/P). State variables are defined as the numerical dispersion and -diffusion observed in the output of the characteristic variables of the lock-exchange experiment. To quantify the errors of interest first the observed results are normalized to the varying parameter as prescribed by the conclusions of the qualitative analysis and similar methods used in literature [@Shin2004; @Adduce2012].**

