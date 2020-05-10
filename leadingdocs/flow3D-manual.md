% Delft Flow-3D FM Manual 
% Instructions and notes

# Possible issues

* RGFGRID 6.02.00.64375 - When creating a rectengular grid with m=100, n=100 and (x,y)=(0,0) as origin one node is not created. When the grid is deleted an created again the error seems to have dissapeared.
* p. 68 - It seems it can not be deleted using backspace but using delete button
* Project tab - properties button does not seem to work


# Command line testcase
If the GUI does not import a testcase correctly try running the following in the commandline:

Windows:
~~~
set OMP__NUM_THREADS=3
"<installation-base-dir>\plugin'DeltaShell.Dimr\kernels\x64\scripts\run_dimr.bat" dimr.xml
~~~

Linux:
~~~
set OMP__NUM_THREADS=3
<installation-base-dir>/lnx64/bin/run_dimr/sh -m dimr.xml
~~~

# Scripting 

- Write general MDU file
    - Import grid
    - Set general settings
    - Set initial condition
    - Set boundary condition

# Technical manual summary

## Governing equation

![DFlowFM-equations](/mnt/c/Users/daank/civiel/BEP/images/DFlowFM-equations.png){#fig:DFlowFM-equations}

### Continuity equation
This is discretized per cell by stating the change of volume is equal to the negative sum over all faces j of cell k, of the velocity u-j times the area A-u,j in the direction s-j,k that accounts for the orientation of the face j with respect to cell k. In short:

δV/δt = - ∑(j) A-j ∙ u-j ∙ S-j

### Momentum equation
This is discretized at the faces in face-normal direction. The water level is stored at the cell circumcenters and reconstructed at the faces using an upwind discretization.

#### Advection & Diffusion
The discretized advection-diffusion equation can be found on page 43 of @DFlowTechMan, which uses an implicit and explicit scheme.

Because of the explicit time integration of the momentum diffusion there is a limitation on the timestep, however, in D-Flow this is implemented as a limitation on the eddy viscosity coefficient.

## Boundary conditions

With respect to the domain an infinite domain should be the goal.

Different boundary conditions may be chosen within D-Flow. These boundary conditions can be divided into three groups:
- Boundary conditions that complement the governing equations; continuity and momentum conservation.
- Supplementary boundary conditions that impose additional constraints at a boundary.
- Boundary conditions for constituents, such as salinity

## Numerical scheme
The discretized PDE's are solved by Gaussian elemination up to a maximum degree, a parameter that can be set, after which the resulting diagonally dominant, symmetric matrix is solved by the Conjugate Gradient method. Before the CG method is applied the matrix is preconditioned in order to assure a fast convergence of the CG method. Two methods can be used for this preconditioning:
- Using the Jacobi preconditioner the diagonally dominant matrix is preconditioned by a matrix consisting only of the diagonal of the original matrix.
- Using the LU decomposition preconditioner lower- and upper triangular matrices (L, U) are formed that enable a solving the matrix by Ux = y and Ly = b. However these matrices may be a lot less sparse then the original matrix which would cause an increase in memory usage. To overcome this problem the maximum degree parameter in D-Flow may be set.

[@DFlowTechMan p.21]

(Possibly incomplete LUD is applied where L and U are matrices with a same sparsity pattern as the original matrix are formed such that LU ≈ A. The matix M = LU is then used to precondition (L, U). The matix M = LU is then used to precondition the original matrix before CG is applied.)

## Turbulence
### Reynold stresses
Horizontal viscosity can be divided into three contributing parts:
- sub grid scale turbulance
- 3D turbulence
- dispersion for depth averaged simulation

### Viscosity
Modelling horizontal eddy viscosity has three seperate parameters that determine the total viscosity as follow: μ-H = μ-sgs + μ-v + μ-H-back.

These three parameters account for the following:
- Horizontal turbulent viscosity may be underestimated because of the sub-grid scale turbulent motions, i.e. turbulence on a scale smaller than the meshgrid. This can be resolved by the sub-grid scale viscosity: μ-sgs
- With Reynolds averaged shallow water equations horizontal eddy viscosity might not accounted for (enough) either thus D-Flow introduces the  μ-v. 
- If extra constant or spatially dependant viscosity is desired the background viscosity μ-back may be added. 

With respect to the 3D viscosity resulting from three-dimensional turbulence a closure model is used [@DFlowTechMan, p.26]. For specific closure models one can even account for unresolved mixing through an ambient background mixing coefficient μ-V-back. Eventually the vertical eddy viscosity is thus calculated by a combination of the 3D viscosity μ-v and μ-mol, the latter being the kinematic viscosity of water, as follows: μ-v = μ-mol + max(μ-v, μ-v-back).

In D-Flow FM four turbulence closure models can be chosen, the first being user defined and the latter three based on models by Kolmogorov and Prandtl, all are explained in further detail in [@DFlowTechMan, p.112-120]; 
- Constant coefficient - resulting in a parabolic vertical velocity profile
- Algebraic eddy viscosity closure model - based on the von Karman constant (κ), the bed friction (Cf), without including transport processes, computing mixing lenght (L), the shear velocity and the vertical turbulent viscosity μ-v. 
- Κ-ε turbulence model - involves solving a non-linear coupled system of equations describing turbulent kinetic energy (Κ) and energy loss (ε) including diffusivity coefficients (D), a turbulent kinetic energy production term (P), a Buoyancy flux (B) and a variation of kalibration terms (c1-3). Therafter the the vertical eddy viscosity μ-v is determined as proportianal to the ratio Κ²/ε and the mixing lenght. Still, this coupled system has to be discretized in terms of advection and diffusion which is done explicitly by a first order upwind scheme and implicitly, respectively. Accordingly the production and buoyancy term are discretized while conserving the diagonally dominant matrix (ensuring positivity). Finally this leads to two tri-diagonal matrices for Κ and ε that can be solved using Thomas algorithm, which may be seen as the tri-diagonal LU-decomposition, by using specific boundary conditions. 
- Κ-τ turbulence - Where τ is a typical timescale of the turbulent eddies and the eddy viscosity is proportional to Κ∙τ. Coupled by a system of convection diffusion equations including diffusivity, production and buoyance terms. The resulting advection equation is discretized with an first order upwind difference scheme and the vertical diffusion term is discretized implicitly by a temporal discretization scheme. Again this leads to two tri-diagonal matrices that can be solved by the Thomas algorithm using specific boundary conditions.


## Hydrostatic model
The model is hydrostatic thus vertical accelerations are not taken into account. The pressure is assumed to vary linearly at each cell along the vertical direction depending on the density state of the cell, related to the temperature and salinity. [@DFlowTechMan, p.121]

## Bed friction and wind friction coefficients 


## Higher order reconstruction

Higher order accurate discretization of the advection may be realized by a higher order accurate reconstruction of the face based full velocity vectors. By default a first order approximation is used. But if the limtypmom variable is specified a limitier is used to obtain a total variation diminishing scheme (TVD). 


# Initias settings
- Lengteschaal: Tussen de monding (ter hoogte van hoek-van-holland) en verder bovenstrooms (ter hoogte van Krimpen aan de lek) kan via Rijkswaterstaat een saliniteit van respectievelijk +/- 4500 en +/- 100 mg/l worden waargenomen. Dit is over een afstand van ongeveer 40km. Deze situatie zullen we als vuistregel nemen voor de initiele test. 

- 

# User manual

General settings:
- significant number can be set

Timeframe
- CFL condition
- initial and max timestep
- period
- Secondary flow
- Wave model 
- Temperature

