# Time dilation
Modul mms.experiment1 is simulate kinematic relitivistic effects.
  
## 1. Experiment description  
Table 1. Measure result for v = 0.4  
countTick= 7 sizeTick= 10  
Particle_velosety= 5 ,i.e= 0.5 [m]/[m]  
Time count = 70  
Particle velosety = 5  
nu_t = 10.0 , nu_x = 10.0 , nu_m = 1.0  
mass = 1 , lightVel = 1.0  
  
  
## 2. Results of experiment
In Table 1 is depicted result of simulation.  
  
```
Trajectory of particle and local time
+----+-----+-----+------+------+
| Tw |  x  |  t  |  ta  | err% |
+----+-----+-----+------+------+
| 0  | 0.0 | 0.0 | 0.0  | 0.0  |
| 1  | 0.5 | 1.2 | 1.12 | 7.33 |
| 2  | 1.0 | 2.3 | 2.24 | 2.86 |
| 3  | 1.5 | 3.4 | 3.35 | 1.37 |
| 4  | 2.0 | 4.5 | 4.47 | 0.62 |
| 5  | 2.5 | 5.6 | 5.59 | 0.18 |
| 6  | 3.0 | 6.8 | 6.71 | 1.37 |
+----+-----+-----+------+------+
```
  
Column gTime is number of step (button "Tick"). Column Time-Anl is analytic calculation to formula t = sqrt(s2+x2). Column Time is t0, i.o. time in motionless frame of reference. Column x - coordinate of particle in moment gTime. Column pTime is time of particle. Column localTime is local time in cell x.



![Fig1](Figure3-1-3.png)  
Figure 1. A Minkowski spacetime diagram 

We observe time dilation. In particle, elapse tp units of time but in motionless frame of reference register tobs units of time.
Following is an example of a graphic and caption (“Figure” style).

We processing of data and calculate of incline k (green line)

and
  
```
Analytical incline k_an= 2.24 ,1/v= 2.0
pair points method (d=4)
0 20 45 2.25
1 20 44 2.2
2 20 45 2.25
Point count = 3
Measurement incline k_ar= 2.23 ,k_err%= 0.12
k_ar = 2.23 +/- 0.017
Experimental error of measurement t is  0.05
```  

In case of small velocity, graph depicted in Fig.6

## 3. Description of experiment3 modul
  
### Class "freeMotion"  

Description: the class is a simulation model  
Bases: mms.Composite  
`def __init__(self, sizeTick, countTick, particle_velosety, observer)`    
Name | Type | Description  
---- | ---- | ----------- 
sizeTick | int | size of time tact
countTick | int | count of tacts
particle_velosety | int | inicial speed particle
observer | Table instance | Detector and recorder


Operations:

def interaction(self, car)
Description: none interaction
Parameters: "car" is "Currer" instance  

### Class "originalToolkit"

Description: new procedures join to processor of data
Bases: ResacherInstruments.DataProcessing
`def __init__(self, observer,particle_velosety, sizeTick, countTick)`
  
Name | Type | Description  
---- | ---- | ----------- 
observer | Table instance | Detector and recorder
particle_velosety | int | inicial speed particle
sizeTick | int | size of time tact
countTick | int | count of tacts
  
#### Operations:      
**def incline(self)**  
Description: incline k calculate and error  
Parameters: None  
  
Algorithm: 
  
$$
\begin{align*} 
x = \frac{mc^2}{qE} \Big( \sqrt{ 1 + (\frac{qEt}{mc})^2 } -1 \Big)  \\  
v = c \sqrt{\frac{(qEt/mc)^2}{1+(qEt/mc)^2} }   \\  
\end{align*} 
$$  
