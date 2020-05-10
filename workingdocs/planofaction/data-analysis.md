% Data analysis
# Indicator parameters
From phase 2 onwards the indicator parameters will be compared to the obtained result in order to get insight into the model and how it behaves. The following parameters will be used as indicators:

    * Reynolds number

    * Froude number

    * Diffusivity and viscosity (η = ρ∙D = ρ∙μ)

## Numerical conditions
In order to analyze the numerical results and qualitatively be able to explain why certain behaviour is observed the numerical schemes will be analyzed according to common conditions and parameters used to asses the consistency, stability and convergence of numerical methods and schemes. 

### Consistency, stability and convergence of finite differences

1. If the local truncation error goes to zero in the limit of Δx a finite difference scheme is called consistent.

2. If there exists a constant C independant of Δx such that the norm of matrix A stays smaller than C if Δx goes to zero, a finite differences scheme is called stable.

3. If the global truncation error goes to zero as Δx goes to zero a scheme is called convergent. This happens if the scheme is both consistent and stable. 

[@Vuik2007]

### Condition number
The condition number Κ of a matrix A is defined as the ratio between the relative error in the approximation (Δw/w) given a relative error in the right hand side of the matrix equation (Δf/f). For symmetric matrices this number is equal to the magnitude of the maximum eigenvalue divided by the magnitude of the minimum eigenvalue: Κ = |λmax|/|λmin|. This range of eigenvalues can be estimated using Gershgorin circle theorem [@Vuik2007, p.107]. 

Using a more realistic estimation of the relative error in the approximation one can obtain the effective condition number defined as: Κ-eff = 1/λmin ∙ |f|/|w|.

### Other conditions
The conditions below will be discussed further if they turn out to be relevant.

    * Von Neumann condition (Amplification factor)
    * CFL condition (Positive numerical diffusion, domain of influence)
    * Computational stability (Domain of influence)
    * Heuristic stability 
    * Monotonicity

[@zijlema_computational_2015]

#### Spectral analysis
If significant numerical dispersion is observed a spectral analysis may be performed as proposed by @Ruano2019.

#### Interval analysis
To deal with uncertainties in model parameters an interval analysis may be done. Also to attain a range of values for certain parameters. 

## Variable leverage
Eventually after the data analysis the sensitivity of the numerical diffusion and dispersion produced by the model to a number of chosen parameters can be produced. A distinction will be made between model parameters, forcing and submodels in order to separate the grounds on which conclusions can be drawn. 

    * Parameters

    * Forcing 

    * Submodels


