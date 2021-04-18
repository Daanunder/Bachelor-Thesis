% General summary of sources

# Numerical math

## Finite differences
![finite-differences](/mnt/c/Users/daank/civiel/BEP/images/finite-differences.png){#fig:finite-differences}
[@AMS]

## Numerical dispersion

If the central difference method is used to obtain a solution for the convection-diffusion equation, which has a monotonically increasing analytical solution, ocscillations in the approximation are by definition erroneous. This is called numerical dispersion and can be avoided by using an upwind difference method to approximate the convection term. 

## Numerical diffusion
If an upwind difference scheme is used in order to obtain physically realistic behaviour in the approximation of an advection-diffusion problem (e.g. to ensure monotonicity) the order of accuracy is decreased. As explained in [@Vuik2007 p. 113-114]

## Convergence and mesh independence study
Results obtained from the D-Flow FM model are the results of a numerical approximation specific to the meshgrid defined in the posed problem. Therefore the convergence of the solution and the independency of it's results to the meshgrid needs to be analyzed. 

With respect to convergence of the model the output can be analyzed according to three points:
- Residual Mean Squared Error
- Gradient at monitor points (and observed parameters) 
- Imbalance of the computation (Global sum of a parameter

A grid independence study is well depicted by plotting number of cells vs. value at monitoring points. However it may be expected that a relatively acceptable tolerance might not be attained given the limitations the numerical model poses on the gridsize in combination with the timestep.

## Spectral analysis
If significant numerical dispersion is observed a spectral analysis may be performed as proposed by @Ruano2019

## Interval analysis
To deal with uncertainties in model parameters an interval analysis may be done. Also to attain a range of values for certain paramters.

## Condition number
The condition number Κ of a matrix A is defined as the ratio between the relative error in the approximation (Δw/w) given a relative error in the right hand side of the matrix equation (Δf/f). For symmetric matrices this number is equal to the maginitude of the maximum eigenvalue divided by the magnitude of the minimum eigenvalue: Κ = |λmax|/|λmin|. This range of eigenvalues can be estimated using Gershgorin circle theorem [@Vuik2007, p.107]. 

Using a more realistic estimation of the relative error in the approximation one can obtain the effective condition number defined as: Κ-eff = 1/λmin ∙ |f|/|w|

## Consistency, stability and convergence of finite differences

1. If the local truncation error goes to zero in the limit of Δx a finite difference scheme is called consistent.

2. If there exists a constant C independant of Δx such that the norm of matrix A stays smaller than C if Δx goes to zero, a finite differences scheme is called stable.

3. If the global truncation error goes to zero as Δx goes to zero the a scheme is called convergent. This happens if the scheme is both consistent and stable. 


# Modelling of flow and transport [@Battjes2017]

## Molecular diffusion
As emphasized by [@Battjes2017, p194]: "..molecular diffusion is irrelevant in civil engineering practice, where turbulent diffusion and dispersion are dominant..". 

In this case however it could be relevant because of the specific experiment. Still with the goal of modelling the Rhine-Maas delta in mind emphasis may be put on diffusion and dispersion processes related to turbulence. 

## Turbulent diffusion
To describe the turbulent diffusion the fluctuating quantaties are averaged over a certain time and lenght scale. Because of gravity the concentration gradient is positive in the downward z-direction. From the averaging of the turbulent motion and the gravity induced concentration gradient it follows, as quoted from [@Vuik2007, p.197], that: "..turbulent fluctuations cause a mean transport in the direction of decreasing values of the mean concentration, as in a diffusion process."

Because the fluctuating quantities cause such net transport processes, the resulting motion and turbulent properties need to be quantified. To this end @Prandtl1925 defined the concept of mixing lenght that defines the lenght over which the fluctiations cause a deviation from the average state and correspond to the average distance the turbulence eddies travel. For example, velocity fluctuations can be related to the velocity of the turbulent eddies. Further the turbulence induced transport processes are found to be proportional to the concentration gradient, also called the turbulence diffusivity. It has the order of magnitude of the eddie velocity times the mixing lenght.

For vertical diffusion in free surface flows the mixing lenght changes over the depth since it is induced by the bed friction expressed in the bed shear stress (τ-b). Using his an estimate of the particle velocity can be made by the so-called shear velocity which together with a parabolic variation of the mixing length over the depth gives a measure for the turbulence diffusivity: εt = Κ∙u∙L = Κ∙u∙z∙(1 - z/d). Where Κ is the Von Karman coefficient which was previously empirically determined.

In exactly this manner horizontal momentum can be vertically distributed through so-called Reynolds shear stress (τ-xz). Thus, in this case it is not a concentration (c) but a momentum per unit volume (ρu) that is diffused, an effect referred to as eddy viscosity. In a simple free surface flow [@Vuik2007, p.199] shows how this leads to a logarithmic velocity profile.

## Longitudal transport

## Lateral transport

## Two dimensional Advection-Diffusion equation*

## Characterisics based methods 
If the wave caused by 


# Gravity currents produced by lock exchange [@Shin2004]

Paper essence: Dissipation in mixing is unimportant when the Reynolds number is sufficiently hight because the energy dissipated is small.

In contrary to Benjamin (j. Fluid Mech. vol 31, 1968, p. 209)

Proposes alternative theory that predicts current speed and depth based on energy conserving flow. 

Froude number = 1 and not √2. 

## Introduction
A lock exchange experiment is explained

γ = density ration = ρ1 / ρ2

Speeds of the buoyant and gravity current are almost the same and linear over x/H per t (where t is dimensionless time being: t = √(t∙(1-γ)/H))

Benjamin (1968) derived a range of solutions depending on the depth of the current that can be formed with a control volume with a frame of reference equal that moves with the speed of the frontal wave speed. If energy conservation within the volume is assumed one realistic solution remains that predicts the wavespeed given the currentdepth is equal to half of the waterdepth. Experiment show that this solution is sufficiently accurate even in situations where energy dissipation is clearly present. Gardner & Crow (1970) and Wilkinson (1983 made this evident and even extended the theory to include surface tension effects. 

Smoothness of the (free or mixing) surface, or in the case of a dual density fluid the contact surface / mixing front, implies little loss of energy. 

Important parameters used in this model:
- dimensionless speed as froude number - Fh = U / √(g'H) with g'=g(ρ2-ρ1)/ρ2. 

Benajmin's theory (1968) predicts Fh = 0.5. Keulegan (1958) finds that the current speed is independent of width/depth ratio. 

Most results (Keulegan 1958, Barr 1967) show Fh increase with Reynolds number. 

Von Karman (1940) gives an indication for an energy conserving current propagating in an ambient fluid of infinite depth. He predicts the frontal wave speed to be: Fh = U/√(g'h) = √2/γ. With h being the depth of the current. Which is confirmed by Benjamin.


# The use of TVD Limiters for Forward-in-Time Upstream-Biased Advection Schemes in Ocean Modelling
TVD based limiters are used for a three-dimensional version of a forward-in-time advection scheme.

Second order accurate on smooth solutions but can deal with discontinuitites without spurious oscillations

Higher order schemes are compared by Zalesak (1987), which distinguishes the conservative Godunov schemes and algebraic schemes with flux limiters (TVD). 

Multiple sources (Carpenter et al. (1990), Xue and Thorpe (1991), Line et al. (1994), Line and Rood (1996)) have found godunov schemes (Monotone upstream centered (2nd O) and piecewise parabolic(3rd O) can be used to model large scale problems. 

On the other hand flux-limited forward-in-time are shown to succesfully model large scale constituent transport problems. (Godunov scheme with Forward Euler and TVD limiter). (Thuburn (1993), Hundsdorfer and Spee (1995)).

Hundsdorfer and Trompert (1994) showed good results for two dimensional modelling of a front using a forward-in-time upstream-biased advection scheme. 

A number of flux limiters are compared, these are nonoscillatory versions of the constant grid flux form scheme. "The PDM limiter is found to give best overall results for one and two dimensional test cases." 

The study has the goal to investigate and improve advection fields at locations of sharp gradients in three-dimensional large scale modelling using a leapfrog scheme with a constant grid and flux limiters.












