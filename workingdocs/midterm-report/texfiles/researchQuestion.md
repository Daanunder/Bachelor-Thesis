% Research Question & Hypothesis
# Research questions

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

# Hypotheses
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

