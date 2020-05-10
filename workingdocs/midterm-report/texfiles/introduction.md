% Introduction

Due to temperature and salinity differences density driven currents can occur. Because important water systems such as the drinking water supply and large coastal systems in the Netherlands are strongly influenced by these currents it is important to understand these phenomena. With the use of D-Flow FM, a software package by Deltares, the mixture of salt- and fresh water can be numerically approximated. However, a side effect of these numerical flow models is the occurrence of numerical diffusion and dispersion caused by characteristics of the numerical discretization scheme that is used.

# Numerical diffusion and -dispersion
Numerical diffusion is sometimes referred to as "numerical viscosity" since the associated approximation errors mimic the effect of an increase in viscosity, i.e. the solution is overdamped. Since viscous properties of a fluid decrease the amplitude of the diffusivity rate in advection-diffusion flow problems. Additionally, numerical dispersion is related to unrealistic oscillations in an approximation of an advection-diffusion problem that may occur if stability of the solution is not ensured or if the observed phenomena are not smooth enough for the discretized solutions of the problem posed. Because avoiding such errors requires contrasting measures a quantification of their responses to certain modelling parameters is desirable. [@zijlema_computational_2015; @obrien_study_1950]

# Lock-exchange experiment
In order to quantify the numerical diffusion and dispersion terms in the D-Flow FM model, and thus get an idea of the model's sensitivity to certain parameters, a lock-exchange experiment will be set up which serve as the basis for a sensitivity analysis. A lock-exchange consists of a closed fluid-tank which can initially be divided into two volumes, one with a higher density than the other seperated by a impermeable boundary. At the beginning of the experiment this boundary is abolished after which the heavier fluid experiences a gravity induced flow and the lighter fluid (or possibly even gas) experiences a buoyency induced flow. In this case an experiment with two fluids with an equal initial waterdepth but different densities, due to a alinity difference, will be setup. 

# D-Flow FM
Shallow water equations: Vertical velocity is small compared to horizontal scale. Vertical pressure nearly hydrostatic. Wave induced accelerations in the vertical cause negligible effect on the pressure distribution compared to the wave induced height difference. 

Shallow water equations show the water mass density is directly proportional to bed- and wind friction terms. (p. 35)


# Method
## Problem definition
After an initial qualitative analysis of the terms and settings found during an explorative setup of the basic D-Flow FM model, a stable basis for the sensitivity analysis will be defined. This includes the variable ranges over which the chosen parameters will be defined and also the reference model to which the results will be compared. Among others, in this basic model setup the desired boundary conditions, the lenght and timescale of the simulation, the constant parameters and general modelling characteristics will be determined. For further specification of this basic setup see [@ Herafter the creation of such basic model will be automated so that the data required for the sensitivity analysis may be generated.

## Research objective
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
       
# Literature
**Insert results found in literature and related research**
