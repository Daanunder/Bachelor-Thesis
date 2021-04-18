# Modelling of flow and transport
## Molecular diffusion
As emphasized by [@Battjes2017, p194]: "..molecular diffusion is irrelevant in civil engineering practice, where turbulent diffusion and dispersion are dominant..". 

In this case however it could be relevant because of the specific experiment. Still with the goal of modelling the Rhine-Maas delta in mind emphasis may be put on diffusion and dispersion processes related to turbulence. Moreover it is assumed constant accross the experiment thus numerical errors can not be specifically dedicated to the diffusion.

## Turbulent diffusion
To describe the turbulent diffusion the fluctuating quantaties are averaged over a certain time and lenght scale. Because of gravity the concentration gradient is positive in the downward z-direction. From the averaging of the turbulent motion and the gravity induced concentration gradient it follows, as quoted from [@Vuik2007, p.197], that: "..turbulent fluctuations cause a mean transport in the direction of decreasing values of the mean concentration, as in a diffusion process."

Because the fluctuating quantities cause such net transport processes, the resulting motion and turbulent properties need to be quantified. To this end @Prandtl1925 defined the concept of mixing lenght that defines the lenght over which the fluctiations cause a deviation from the average state and correspond to the average distance the turbulence eddies travel. For example, velocity fluctuations can be related to the velocity of the turbulent eddies. Further the turbulence induced transport processes are found to be proportional to the concentration gradient, also called the turbulence diffusivity. It has the order of magnitude of the eddie velocity times the mixing lenght.

For vertical diffusion in free surface flows the mixing lenght changes over the depth since it is induced by the bed friction expressed in the bed shear stress (τ-b). Using his an estimate of the particle velocity can be made by the so-called shear velocity which together with a parabolic variation of the mixing length over the depth gives a measure for the turbulence diffusivity: εt = Κ∙u∙L = Κ∙u∙z∙(1 - z/d). Where Κ is the Von Karman coefficient which was previously empirically determined.

In exactly this manner horizontal momentum can be vertically distributed through so-called Reynolds shear stress (τ-xz). Thus, in this case it is not a concentration (c) but a momentum per unit volume (ρu) that is diffused, an effect referred to as eddy viscosity. In a simple free surface flow [@Vuik2007, p.199] shows how this leads to a logarithmic velocity profile.

