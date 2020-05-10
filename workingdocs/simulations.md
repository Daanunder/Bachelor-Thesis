# Simulations log

## 0805-1
### Observations
First simulation is succesful with following parameters, if nothing is specified default is used. The result seems to have innaccuracies at the utterleft boundary for both the velocity and the salinity. For some reason the salinity there decreases. The salinity at the initial disturbance to the boundaries in x-direction diffuses fast (within 400m each direction), also it can only be seen changing in the first 4 hours of the simulation. The velocity profile caused by the disturbance only changes in the first 2 hours of the simulation across a similar distance. The discharge shows hardly anomalies at the left boundary and only shows changes over a distance of approximately 150m each direction. 

### Conclusion
It seems a shorter period for the simulation should be taken, first a shorter max. time step is chosen to verify this conclusion. 


## 0805-2
### Observations
Changed max timestep to 120 seconds. The salinity profile seems unchanged compared to run 08/05/2020-1, still the disturbance around the initial salinity gradient travels over a distance of +/- 300m each direction and an anomaly is observed near the left boundary. However the velocity profile shows changes across the domain in the first 13 minutes, thereafter it still changes untill 160 minutes after the start of the experiment. The discharge shows similar behaviour as the velocity but it contains an anomaly at the location of the initial disturbance. 

## 0905-1
### Observations
Changed the period from 24 to 6 hours but almost the same observations as in the previous runs can be made. The salinity profile only changes over a distance of +/- 300m each direction. However a clear velocity profile develops over the whole 10km in the first 4 minutes, herafter reflections of this profile can be observed. A timestep of 3 to 5 minutes is automatically configured by D-Flow FM. In all runs so far a difference between cells at the edge and in the center was observed as well, this is not desired and unsuspected since a free-slip boundary is configured across all boundaries.

### Conclusion
Change the boundary condition to free-slip to ensure a uniform profile over the width of the model. Try reducing timestep before period to possibly confirm the timestep should be changed, also calculate the expected frontal wavespeed as a reference. Possibly the single layer settings induce the observed behaviour. 

## 0905-2
### Observations
Changed the period to 1.5 hours but the same behaviour is observed. It should also be noted that the reflection of the velocity front is not so much a reflection as it seems more a velocity front developing over the single layer to deal with the initial salinity difference, then when the front reaches the boundary, the velocity profile over the whole model becomes zero and still a density diference remains at the location of the initial disturbance thus the model creates a second velocity front to deal with this difference, this front is smaller. Then a third velocity front is formed, even smaller than the second, and a fourth, and so on untill the density difference is spread as much as the simulation permits.

The water balance errors where in the order of E-7 and the computation timestep increased to 100s the first 15min of the simulation and was a constant 100s until the end of the simulation.

### Conclusion
Because I suspect the model shows the observed behaviour because of the single layer setting this is what will be investigated in the next run. Further also the perid and max. timestep of the first simulation are revived to ensure a consistent iterative process.


## 0905-3
### Observations
The number of layers is set to 3, the period is 24hours and the max. timestep is set to 20min. The salinity profile shows no change, it is unclear why. The velocity profile still shows spurious oscillations, the discharge likewise. after 10hours a realively stabel conditions is reached. 

The computational timestep varies from 0 to 100s in the first 10 minutes, then fluctuates shortly between 100, 75 and 150 untill 2h05min when it stabilizes at 150s. The water balance volume error constantl increases (in absolute sense) from 0 to -6E-4. 

### Conclusion
Possibly the initial conditions need to be reset on the 3-layered grid. This will be investigated.

