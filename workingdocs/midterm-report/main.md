% Final report - first draft

<!-- vim-markdown-toc GFM -->

* [Abstract](#abstract)
* [Introduction](#introduction)
    * [Numerical diffusion and -dispersion](#numerical-diffusion-and--dispersion)
    * [Lock-exchange experiment](#lock-exchange-experiment)
    * [D-Flow FM](#d-flow-fm)
    * [Method](#method)
        * [Problem definition](#problem-definition)
        * [Research objective](#research-objective)
    * [Basic assumptions](#basic-assumptions)
    * [Literature](#literature)
* [Research Question & Hypothesis](#research-question--hypothesis)
    * [Research questions](#research-questions)
    * [Hypotheses](#hypotheses)
* [Method](#method-1)
    * [D-Flow FM setup](#d-flow-fm-setup)
        * [Initial qualitative analysis](#initial-qualitative-analysis)
        * [Refinement of the basic model](#refinement-of-the-basic-model)
        * [Post processing setup](#post-processing-setup)
    * [Data generation](#data-generation)
    * [Data analysis](#data-analysis)
* [D-Flow FM setup](#d-flow-fm-setup-1)
    * [Initial model](#initial-model)
        * [General settings](#general-settings)
        * [Physiscs](#physiscs)
        * [Geometry](#geometry)
        * [Flow](#flow)
        * [Numerics](#numerics)
        * [Meshgrid](#meshgrid)
        * [Monitoring points](#monitoring-points)
    * [Qualitative analysis](#qualitative-analysis)
        * [Extreme values](#extreme-values)
        * [Characteristic locations](#characteristic-locations)
    * [Post Processing](#post-processing)
        * [Normalized results](#normalized-results)
        * [Riemann invariants](#riemann-invariants)
        * [Indicator parameters](#indicator-parameters)
* [Data generation](#data-generation-1)
    * [Defining parameter variation](#defining-parameter-variation)
        * [Interval analysis](#interval-analysis)
        * [Numerical evaluation criteria](#numerical-evaluation-criteria)
    * [Running simulations](#running-simulations)
        * [General settings](#general-settings-1)
        * [Physiscs](#physiscs-1)
        * [Geometry](#geometry-1)
        * [Flow](#flow-1)
        * [Numerics](#numerics-1)
        * [Meshgrid](#meshgrid-1)
        * [Monitoring points](#monitoring-points-1)
    * [Post Processing](#post-processing-1)
        * [Normalized results](#normalized-results-1)
        * [Riemann invariants](#riemann-invariants-1)
        * [Indicator parameters](#indicator-parameters-1)
* [Data analysis](#data-analysis-1)
    * [Sensitivity analyis](#sensitivity-analyis)
        * [Variable leverage](#variable-leverage)
* [Discussion and conclusion](#discussion-and-conclusion)
* [References](#references)
* [Appendix](#appendix)

<!-- vim-markdown-toc -->

# Abstract

# Introduction

Due to temperature and salinity differences density driven currents can occur. Because important water systems such as the drinking water supply and large coastal systems in the Netherlands are strongly influenced by these currents it is important to understand these phenomena. With the use of D-Flow FM, a software package by Deltares, the mixture of salt- and fresh water can be numerically approximated. However, a side effect of these numerical flow models is the occurrence of numerical diffusion and dispersion caused by characteristics of the numerical discretization scheme that is used.

## Numerical diffusion and -dispersion
Numerical diffusion is sometimes referred to as "numerical viscosity" since the associated approximation errors mimic the effect of an increase in viscosity, i.e. the solution is overdamped. Since viscous properties of a fluid decrease the amplitude of the diffusivity rate in advection-diffusion flow problems. Additionally, numerical dispersion is related to unrealistic oscillations in an approximation of an advection-diffusion problem that may occur if stability of the solution is not ensured or if the observed phenomena are not smooth enough for the discretized solutions of the problem posed. Because avoiding such errors requires contrasting measures a quantification of their responses to certain modelling parameters is desirable. [@zijlema_computational_2015; @obrien_study_1950]

## Lock-exchange experiment
In order to quantify the numerical diffusion and dispersion terms in the D-Flow FM model, and thus get an idea of the model's sensitivity to certain parameters, a lock-exchange experiment will be set up which serve as the basis for a sensitivity analysis. A lock-exchange consists of a closed fluid-tank which can initially be divided into two volumes, one with a higher density than the other seperated by a impermeable boundary. At the beginning of the experiment this boundary is abolished after which the heavier fluid experiences a gravity induced flow and the lighter fluid (or possibly even gas) experiences a buoyency induced flow. In this case an experiment with two fluids with an equal initial waterdepth but different densities, due to a alinity difference, will be setup. 

## D-Flow FM
Shallow water equations: Vertical velocity is small compared to horizontal scale. Vertical pressure nearly hydrostatic. Wave induced accelerations in the vertical cause negligible effect on the pressure distribution compared to the wave induced height difference. 

Shallow water equations show the water mass density is directly proportional to bed- and wind friction terms. (p. 35)


## Method
### Problem definition
After an initial qualitative analysis of the terms and settings found during an explorative setup of the basic D-Flow FM model, a stable basis for the sensitivity analysis will be defined. This includes the variable ranges over which the chosen parameters will be defined and also the reference model to which the results will be compared. Among others, in this basic model setup the desired boundary conditions, the lenght and timescale of the simulation, the constant parameters and general modelling characteristics will be determined. For further specification of this basic setup see [@ Herafter the creation of such basic model will be automated so that the data required for the sensitivity analysis may be generated.

### Research objective
To be able to refer the sensitivity of numerical errors produced by D-Flow FM to specific settings and parameters of the model data will be generated and analyzed. The required data consist of the numerical errors produced while changing the grid resolution, the timestep size and parameters related to the flow model. Subsequently the sensitivity S of a parameter P is defined as the relative change of a state variable per change of this parameter: S = (δx/x)/(δP/P). *The state parameters are defined as the difference between the approximation and the analytical solution at predefined monitoring points, also known as the accuracy of the approximation.* **What may we define as the accuracy of the model in terms of numerical diffusion and dispersion? What behaviour of the solutions is expected and what do we see in the produced data?** Prematurely three state parameters are defined; the flow velocity, the density and wave speed. During the explorative model setup and the data generation phase, the observed data is analyzed and compared to certain indicator parameters in order to explain the observed numerical errors. 

*These indicators have previously been found to characterize the significance of certain modelling parameters [@Shin2004] of a discretization scheme. Finally the leverage of parameters, forcing functions and submodules of the model are assessed based on the observed sensitivity for which a possible explanation in terms of the indicators and model characteristics will be sought.*

*This document describes the research questions and hypotheses in the first chapter, subsequently it will describe the research strategy explained above in further detail in chapter two. Lastly, in the appendix a planning for this research project can be found.*


## Basic assumptions
* Hydrostatic pressure
    - Depending on the velocity variations seen near the mixing zone this is a valid approximation, i.e. the solution should be smooth
    - Vertical variations in the velocity may still occur as a result of the continuity equation 
* Resistance can be ignored [@Battjes2017] 
    - Damping of wave amplitude should be as little as possible over the simulation, in this case the energy conserving assumption is most valid
    - Longitudal dispersion and the two dimensional advection-diffusion equation should be investigated [@Battjes2017, p. 202]
* When the above are valid characteristic based methods may be used
    - Possibly normalize the wavespeed 
    - Forcing terms are density based
    - Resistance is a result of bed- friction and mixing viscosity
    - For two state variables the wave depth (d) and velocity (u) in a three dimensional shallow water equation the solution set is a volume in the (d, x, y, t)-space and (u, x, y, t)-space
* By examening the flow based on the above assumptions numerical errors may be be recognized:
    - The hydrostatic assumption is least valid at t=0 because of the hydrostatic diferences between the two sides of the front thus this is where numerical diffusion may be at its extreme
    - Resistance may be of significant influence at the mixing layer, especially where internal waves are formed, thus numerical diffusion may be significant 
    - Where the propagation of the disturbance does not follow the expected propagation in the s-t plane (probably is too damped) diffusion may be recognized
       
## Literature
**Insert results found in literature and related research**

# Research Question & Hypothesis
## Research questions

1. How much numerical diffusion and or dispersion does the D-Flow FM model produce when simulating a 3D lock-exchange experiment?

    1. What is the order of errors produced by D-Flow FM as a result of numerical diffusion and/or dispersion?

    2. How sensitive is the accuracy of the D-Flow FM model to time, space and numerically related parameters?

    3. What sort of errors are produced given different parameters?

    4. What parameters in the D-Flow FM model have the largest influence on errors related to numerical diffusion and dispersion?

    5. Are there indicators that predict the occurrence of numerical diffusion and dispersion in D-Flow FM?
    
    6. How do the fysics around the mixing layer develop and what influence does this have on the accuracy numerical approximation in terms of numerical diffusion and -dispersion?

    7. How does the frontal wave speed develop compared to solutions that might be expected from the characteristic equations?

    8. How do internal waves develop at different model parameters and settings?

    9. What effect do internal waves have on the produced numerical errors?

## Hypotheses
1. There is significant numerical diffusion and negligible numerical dispersion in the D-Flow FM model when performing a lock-exchange experiment because the hydrostatic assumptions of the shallow water equations, and thus the numerical scheme within D-Flow, can not deal with the initial vertical pressure gradient but accounts sufficiently for the posed boundary conditions. 

    1. The order of errors is of 10E-4

    2. It is very sensitive to time and space related parameters and can be slightly improved by flow model parameters.

    3. Mostly numerical diffusion errors are produced except when more elaborate advection schemes are applied. 

    4. The time step size, grid resolution and viscosity have the larges influence leverage on the accuracy of the model.

    5. Examples of such indicators are the dimensionless Reynolds and Froude numbers or the ratio between the net diffusivity coefficient in the model and the eddy viscosity terms imposed by D-Flow FM. 

    6. The physical process is naturally damped by viscosity thus at some point the higher-order terms that are included in the truncation error of the numerical scheme will become of lesser influence, therefore numerical diffusion and dispersion will reduce over time. I.e. the shallow water equations will fit the flow better if it is more smooth. 

    7. Riemann invariants may be formed for the flow front if the velocity variations far away from the front are negligible and thus the frontal wave speed may be considered to constant along a characteristic. 

    8. When viscosity plays a more important role internal wave can be expected to be greater. This is at high density differences and at high flow velocities. 

    9. The numerical diffusion is increased a lot by the occurence of a lot of internal waves because the approximation is limited in it's vertical velocity gradient by the hydrostatic assumption. 


# Method
Steps to be incorporated in planning:
1. Get familiar with model
    * Tutorials
2. Run initial lock-exchange experiment
    * Setup general settings
    * Setup basic geometry
    * Setup physics & boundary conditions
    * Setup computational grid
    * Setup monitoring points
3. Perform analysis on obtained results 
    * Perform qualitative analysis
4. Refine reference model
    * Refine model based on qualitative analysis
    * Compute Riemann invariants
    * Compute indicator variables 
    * Refine again until desired reference model is obtained
        - **What parameter interval and numerical conditions may be applicable from the section data generation**
5. Automate standard post processing steps
    * Script standard data analysis on results (normalized)
    * Script characteristic (to be expected results)
    * Script indicator parameters (graphs e.g.)
6. Perform data generation
7. Perform data analysis


## D-Flow FM setup
In order to provide a solid basis for the sensitivity analysis the basic model has to be applicable to the research objective and sufficiently robust to enable all parameters to be explored. To ensure a working model first most default settings will be used to set up the lock-exchange model, *this will already require a minimal definition file where general settings, physics, geometry, flow and numerical parameters are set.* Finally, monitoring points have to be set up at logically sound locations within the basic models in order for the subsequent qualitative analysis and post-processing to be relevant. These monitoring points will be formed at locations where anomaliies in the approximation may be found, thus where numerical errors may be observed in extreme forms. This will be around the wave front, the boundary conditions and near the mixing layer where internal waves may form. It can be discuessed whether these points are stationary or whether it is desirable that this frame of reference moves with a certain speed, e.g. the wavespeed of the front. 

### Initial qualitative analysis
For an inital qualitative analysis the state variables and indicator parameters are evaluated at points where they either have an extreme value or where characteristic values of the solution can be expected. This thus depends on the Riemann invariants formed for the particular situation, taking friction and gravitational forcing into account. 

### Refinement of the basic model
Thereafter possibly more realistic physical properties, boundary conditions, a more relevant geometry and specifics of the flow model such as bed friction and the will be defined based on the qualitative analysis of the produced results. This definition of the reference model should be done with the research objective in mind *thus possibly requires setting up three different models for three different mesh grids in order to enable stable testing, at the cost of consistency between models. These trade-offs with respect to the research applicability and generalizability will have to be made.* Refinement of the model may be done by adjusting the parameters below, it should be noted however that some of these are to remain constant:

* Viscosity
* Initial salinity / density difference
* Bed friction
* Lenght scale
* Time scale
* Height / water depth
* Grid generation
    **Near, intermediate and far field characteristics of transport flows**
* Monitoring points
    **Can this be a moving frame of reference, e.g. based on the expected wavespeed**
* Entrainment (mixing terms)
* Advection scheme


### Post processing setup 
Further on the first post-processing of the generated results by the refined model will be performed, in this way the results of the basic model can be processed and evaluated with respect to multiple indicators and the expected flow characteristics. These steps are also scripted so they can easily be used again, besides being selected on relevance. 

* What may be expected based on the characteristic method?
* How can we normalize the obtained results?
* What indicator parametres are of relevance? 


## Data generation
At the start of the data generation the research strategy has almost been fully developed. But some important questions remain.

* Which parameters are interesting to change?
* What range of values should be investigated?
* How many experiments can be run? 

For this a few evaluations can be made with respect to the numerical model and the governing equations:

* Interval analyis
* Numerical conditions
    * Consistency, stability & convergence (Basic Numerical maths)
    * Von Neumann condition (Amplification factor)
    * CFL condition (Positive numerical diffusion, domain of influence)
    * Computational stability (Domain of influence)
    * Heuristic stability 
    * Monotonicity
* If significant numerical dispersion is observed a spectral analysis may be performed as proposed by @Ruano2019

## Data analysis
During the data analysis the results of all the post processing of the different performed experiments are analyzed and a relation between the sensitiviy of the observed numerical errors to certain the change in certain parameters and computeded indicator parameters are sought for based on the model used and the characteristics of the experiment. 

* What indicator parameters are of significance and why? 
* Can the observed sensitivity of the numerical errors in the produced results to a parameter in the indicator parameters be related to the computed indicator parameters?

# D-Flow FM setup

## Initial model
### General settings
### Physiscs
### Geometry
### Flow
### Numerics
### Meshgrid
### Monitoring points

## Qualitative analysis
### Extreme values
### Characteristic locations

## Post Processing
### Normalized results
### Riemann invariants
### Indicator parameters

# Data generation
## Defining parameter variation
### Interval analysis
### Numerical evaluation criteria

## Running simulations
### General settings
### Physiscs
### Geometry
### Flow
### Numerics
### Meshgrid
### Monitoring points

## Post Processing
### Normalized results
### Riemann invariants
### Indicator parameters

# Data analysis
## Sensitivity analyis
### Variable leverage
    * Parameters
    * Forcing 
    * Submodels



# Discussion and conclusion

# References

# Appendix
