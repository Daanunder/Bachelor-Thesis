% Quantifying numerical diffusion and dispersion of the D-Flow FM model using lock-exchange experiments

# Introduction

Due to temperature and salinity differences density driven currents can occur. Because important water systems such as the drinking water supply and large coastal systems in the Netherlands are strongly influenced by these currents it is important to understand these phenomena. With the use of D-Flow FM, a software package by Deltares, the mixture of salt- and fresh water can be numerically approximated. However, a side effect of these numerical flow models is the occurrence of numerical diffusion and dispersion caused by characteristics of the numerical discretization scheme that is used. 

Numerical diffusion is sometimes referred to as "numerical viscosity" since the produced error behaves as an increase in viscosity. Since viscosity decreases the amplitude of the diffusivity rate, numerical diffusion will increase this (amplitude) damping even further. Additionally, numerical dispersion is an effect of the discretization of higher order (non-linear) terms related to the hydrological dispersion relation, which include discretization schemes to deal with advection processes. Errors of this kind are often expressed through physically unrealistic oscillations in the approximation. Because avoiding such errors requires contrasting measures a quantification of their responses to certain modelling parameters is desirable. [@zijlema_computational_2015 @obrien_study_1950]

In order to quantify the numerical diffusion and dispersion terms in the D-Flow FM model, and thus get an idea of the model's sensitivity to certain parameters, a lock-exchange experiment will be set up which will be used as the basis for a sensitivity analysis. After an initial qualitative analysis of the terms and settings found during this explorative setup of the basic D-Flow FM model, the creation of such basic model will be automated. From hereon the data required for the sensitivity analysis will be generated.

The required data consist of the numerical errors produced while changing the grid resolution, the timestep size and parameters related to the numerical discretization scheme. The sensitivity S of a parameter P is defined as the relative change of a state variable per change of this parameter: S = (δx/x)/(δP/P). Three state parameters are defined as the difference between the approximation and the analytical solution at predefined monitoring points, also known as the accuracy of the approximation; the flow velocity error, the density error and wave speed error.  

During the explorative model setup and the data generation phase, the observed data is analyzed and compared to certain indicator parameters that have previously been found characterize the significance of certain modelling parameters [@Shin2004]   of a characterize certain discretization schemes and corresponding truncation errors in order to explain the observed errors. Examples of such parameters are the dimensionless Reynolds and Froude numbers or the ratio between the net diffusivity coefficient and viscosity. Additionally the leverage of parameters, forcing functions and submodules of the model are assessed based on the observed sensitivity. 


# Research Question & Hypothesis
## Research questions

1. What is the order of errors produced by D-Flow FM as a result of numerical diffusion and dispersion for different parameters of the discretization scheme?

2. How sensitive is the accuracy of the D-Flow FM model to time, space and numerically related parameters when applied to a lock-exchange experiment?

3. What parameters in the D-Flow FM model have the largest influence on errors related to numerical diffusion and dispersion?


## Hypotheses
1. The order of errors is of 10E-4
2. It is very sensitive to time and space related parameters and can be slightly improved by numerical parameters.
3. The time step size, grid resolution and viscosity have the larges influence leverage on the accuracy of the model.


# Method

## Model exploration D-Flow FM
    - General settings
    - Physics
    - Geometry
    - Flow
    - Numerics
    - Post-processing
    - Automation
## Data generation
### State variables
    * Flow velocity error
    * Density error
    * Wave speed error
### Spacial sensitivity
    * Parameters
        * Resolution (Δx,Δy,Δz)
        * Water depth
        * Lock lenght
    * Converging solution with an acceptable Residual RMS Error (< 10E-4)
    * Imbalances (< 1%)
    * Achieve grid independance
### Numerical sensitivity
    * Timestep (Δt)
    * Viscosity
    * Flow model parameters
        * Entrainment (mixing terms)
        * Free surface
        * Turbulence parameters
    * Numerical parameters 
        * Advection scheme
        * Central or upstream difference
## Data analysis
### Indicator parameters
    * Reynolds number
    * Froude number
    * Diffusivity and viscosity (η = ρ∙D = ρ∙μ)
    * Numerical conditions
        * Consistency, stability & convergence (Basic Numerical maths)
        * Von Neumann condition (Amplification factor)
        * CFL condition (Positive numerical diffusion, domain of influence)
        * Computational stability (Domain of influence)
        * Heuristic stability 
        * Monotonicity
### Variable leverage
    * Parameters
    * Forcing 
    * Submodels
### Conclusion


# Literature



















