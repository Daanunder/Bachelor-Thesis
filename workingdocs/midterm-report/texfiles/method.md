% Method
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


# D-Flow FM setup
In order to provide a solid basis for the sensitivity analysis the basic model has to be applicable to the research objective and sufficiently robust to enable all parameters to be explored. To ensure a working model first most default settings will be used to set up the lock-exchange model, *this will already require a minimal definition file where general settings, physics, geometry, flow and numerical parameters are set.* Finally, monitoring points have to be set up at logically sound locations within the basic models in order for the subsequent qualitative analysis and post-processing to be relevant. These monitoring points will be formed at locations where anomaliies in the approximation may be found, thus where numerical errors may be observed in extreme forms. This will be around the wave front, the boundary conditions and near the mixing layer where internal waves may form. It can be discuessed whether these points are stationary or whether it is desirable that this frame of reference moves with a certain speed, e.g. the wavespeed of the front. 

## Initial qualitative analysis
For an inital qualitative analysis the state variables and indicator parameters are evaluated at points where they either have an extreme value or where characteristic values of the solution can be expected. This thus depends on the Riemann invariants formed for the particular situation, taking friction and gravitational forcing into account. 

## Refinement of the basic model
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


## Post processing setup 
Further on the first post-processing of the generated results by the refined model will be performed, in this way the results of the basic model can be processed and evaluated with respect to multiple indicators and the expected flow characteristics. These steps are also scripted so they can easily be used again, besides being selected on relevance. 

* What may be expected based on the characteristic method?
* How can we normalize the obtained results?
* What indicator parametres are of relevance? 


# Data generation
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

# Data analysis
During the data analysis the results of all the post processing of the different performed experiments are analyzed and a relation between the sensitiviy of the observed numerical errors to certain the change in certain parameters and computeded indicator parameters are sought for based on the model used and the characteristics of the experiment. 

* What indicator parameters are of significance and why? 
* Can the observed sensitivity of the numerical errors in the produced results to a parameter in the indicator parameters be related to the computed indicator parameters?

# D-Flow FM setup

# Initial model
## General settings
## Physiscs
## Geometry
## Flow
## Numerics
## Meshgrid
## Monitoring points

# Qualitative analysis
## Extreme values
## Characteristic locations

# Post Processing
## Normalized results
## Riemann invariants
## Indicator parameters


