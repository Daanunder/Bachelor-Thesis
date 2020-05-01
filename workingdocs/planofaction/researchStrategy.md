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

