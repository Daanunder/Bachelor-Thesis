% Data generation

In the third phase of the research, the research strategy is completely developed and provides a way to generate the data required to test the hypotheses, which is threefold and dependent on given parameter ranges:
    - Analytical (exact) reference data at monitor points

    - Results obtained from the model

    - Indicator parameters based on the results and input parameters

## State variables

In order to define the sensitivity of the model to certain parameters, the sensitivity S of a parameter P is defined as the relative change of a state variable per change of this parameter: S = (δx/x)/(δP/P). 

It seems that possibly one state variable would be enough which would be the velocity. Yet it would be interesting to see if there is significant molecular diffusion and thus measure the density as a state variable. Also the negative and positive wave of the fluid with a higher density will have a wave speed that might be to analyze because of it's possible relation to the tide induced translatory wave in the Rhine-Muese delta. 
    - Flow velocity error

    - Density error

    - Wave speed error

**It is also important to notice that it is still unknown how the analytical solutions at the monitor points can be calculated.**

## Spacial sensitivity

A very important parameter in the flexible mesh is the resolution of the grid and the sort of mesh used. In order to get a complete analysis of numerical diffusion and dispersion errors in D-Flow FM this should be elaborately evaluated. With respect to the grid three evaluation criteria can be seperately evaluated to assess the applicability of the results obtained from a model. 

    * Is the solution converging with an acceptable Residual RMS Error (< 10E-4)

    * Are the imbalances of the results sufficiently small (< 1%)

    * Achieve grid independence

### Convergence & grid independency
Results obtained from the D-Flow FM model are the results of a numerical approximation specific to the mesh grid defined in the posed problem. Therefore the convergence of the solution and the independency of it's results to the mesh grid needs to be analyzed. 

With respect to convergence of the model the output can be analyzed according to three points:

- Residual Mean Squared Error

- Gradient at monitor points (and observed parameters) 

- Imbalance of the computation (Global sum of a parameter

A grid independence study is well depicted by plotting number of cells vs. value at monitoring points. However it may be expected that a relatively acceptable tolerance might not be attained given the limitations the numerical model poses on the grid size in combination with the timestep and the viscosity. 



## Numerical sensitivity

Another major parameter is the time step size of the approximation. The discretized advection-diffusion equation can be found on page 43 of @DFlowTechMan, which uses an implicit and explicit scheme. Because of the explicit time integration of the momentum diffusion there is a limitation on the time step, however, in D-Flow this is implemented as a limitation on the eddy viscosity coefficient. 

In general the turbulence and diffusion model parameters seems to have a great influence on the calculation complexity of the model. Therefore in appendix A an elaborate explanation of diffusion and turbulence modelling is given including the way D-Flow FM deals with this. Because turbulence, shear stresses and viscosity are similar processes all expressed in diffusivity terms they are grouped in the appendix for brevity. 

In general the following parameters of the numerical model can be evaluated:
    * Timestep (Δt)

    * Viscosity

    * Flow model parameters

        * Entrainment (mixing terms)

        * Turbulence parameters

    * Numerical parameters 

        * Max. degree

        * Conditioner

        * Advection scheme


### Numerical scheme
A short description of the numerical solving process implemented by D-Flow can be explained as follows. The discretized PDE's are solved by Gaussian elemination up to a maximum degree, a parameter that can be set, after which the resulting diagonally dominant, symmetric matrix is solved by the Conjugate Gradient method. Before the CG method is applied the matrix is preconditioned in order to assure a fast convergence of the CG method. Two methods can be used for this preconditioning:
- Using the Jacobi preconditioner the diagonally dominant matrix is preconditioned by a matrix consisting only of the diagonal of the original matrix.
- Using the LU decomposition preconditioner lower- and upper triangular matrices (L, U) are formed that enable a solving the matrix by Ux = y and Ly = b. However these matrices may be a lot less sparse then the original matrix which would cause an increase in memory usage. To overcome this problem the maximum degree parameter in D-Flow may be set.

[@DFlowTechMan p.21]

(Possibly incomplete LUD is applied where L and U are matrices with a same sparsity pattern as the original matrix are formed such that LU ≈ A. The matix M = LU is then used to precondition (L, U). The matix M = LU is then used to precondition the original matrix before CG is applied.)