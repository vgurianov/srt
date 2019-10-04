# Velocity, momentum, and energy
Modul experiment3.py simulate dynamic relativistic effects.  
  
## 1. Experiment description
We consider motion of charge *q* in constant electric field \\( \mathcal{E} \\). Motion equation is  

\begin{equation}
    \frac{dp}{dt} = q \mathcal{E}  \\
\end{equation}
  
where *p* - particle momentum, \\( q \mathcal{E} \\) - force.  
Initial condition is *x* = 0, *p* = 0 in moment *t* = 0.  
If t > \\(z = mc/q \mathcal{E} \\) then appear relativistic effects.  
References: Charles Kittel, Walter D.Knight, Malvin A. Ruderman, Mechanics. Berkeley physics course. Vol.1, McGraw-Hill book company. 1965  
  
We find dependence  
- particle coordinate x from time t
- particle velocity v from momentum p
- particle energy E from momentum p.  

Estimated calculation for electron:  
m=  \\(9.1 \times 10^-31\\)  kg, q=  \\(1.602 \times 10^-19\\) C  
We consider simple case when \\(\mu = 1\\)  (*Skip* list is NULL) and \\(\iota = 1\\) (one act of interaction in tick),    
then  
nu_m =  1.1e+30, nu_t =  3e+9 
f= 2.7e-23  N, \\( \mathcal{E} \\) = 1.7e-4  V/m,  
z =  10.0 s,  
d =  4.14  m  
 
  
In c = 1, m = 1 units system, 
  
\begin{equation}
    \frac{dp}{dt} = \frac{qE}{mc}  
\end{equation}
  
and f = 0.1, \\(\nu_{t} = 10, \nu_{x} = 10\\)  
  
Parameters of computing is m = 1 (rest mass particle), \\( q \mathcal{E} \\) = 0.1  
Variable values:  
countTick= 8, sizeTick= 10  
Particle velosety = 0  (initial velocity)  
nu_t = 10.0 , nu_x = 10.0 , nu_m = 1.0  
mass = 1 , lightVel = 1.0  
  
With this resolution, you can perform 8 clock cycles of the system (if Tw = 9 then an error typical of relativistic models arises, which can be called “synchronization failure”).  


## 2. Results of experiment

The results experiment are shown in Table 1. It is trajectory of particle. 
```
Analytical (xa, pa, va) and numerical (xe) solution
+----+-----+-----+------+------+------+------+-----+------+
| Tw |  t  |  x  |  xa  |  xe  |  p   |  pa  |  v  |  va  |
+----+-----+-----+------+------+------+------+-----+------+
| 0  | 0.0 | 0.0 | 0.0  | 0.0  | 0.0  | 0.0  | 0.0 | 0.0  |
| 1  | 1.1 | 0.1 | 0.06 | 0.12 | 0.11 | 0.11 | 0.0 | 0.11 |
| 2  | 2.1 | 0.3 | 0.22 | 0.33 | 0.21 | 0.21 | 0.0 | 0.21 |
| 3  | 3.1 | 0.6 | 0.47 | 0.62 | 0.31 | 0.31 | 0.0 | 0.3  |
| 4  | 4.2 | 1.0 | 0.85 | 1.05 | 0.42 | 0.42 | 0.0 | 0.39 |
| 5  | 5.3 | 1.5 | 1.32 | 1.56 | 0.53 | 0.53 | 0.0 | 0.47 |
| 6  | 6.4 | 2.1 | 1.87 | 2.16 | 0.64 | 0.64 | 1.0 | 0.54 |
| 7  | 7.6 | 2.8 | 2.56 | 2.88 | 0.76 | 0.76 | 1.0 | 0.61 |
| 8  | 8.8 | 3.6 | 3.32 | 3.67 | 0.88 | 0.88 | 1.0 | 0.66 |
+----+-----+-----+------+------+------+------+-----+------+
```  
Values t,x,p, and v are measurement data, values xa, pa, va are analitical solution (see class "originalToolkit"), xe - numerical solution.  
Following is plot of trajectory (Fig.1).
![Fig1](Fig3-3-1.png)  
Figure 1. Motion plot  
  
The data are presented so that speed and energy can be considered as functions of the momentum.  
```  
Velocity end energy of particle as function from momentum  
+----+------+------+------+--------+------+------+--------+
| Tw |  p   |  v   |  va  | v,err% |  E   |  Ea  | E,err% |
+----+------+------+------+--------+------+------+--------+
| 0  | 0.0  | 0.0  | 0.0  |  0.0   | 1.0  | 1.0  |  0.0   |
| 1  | 0.11 | 0.09 | 0.11 | 16.86  | 1.01 | 1.01 |  0.39  |
| 2  | 0.21 | 0.2  | 0.21 |  2.68  | 1.03 | 1.02 |  0.8   |
| 3  | 0.31 | 0.3  | 0.3  |  1.32  | 1.06 | 1.05 |  1.25  |
| 4  | 0.42 | 0.36 | 0.39 |  6.09  | 1.1  | 1.08 |  1.42  |
| 5  | 0.53 | 0.45 | 0.47 |  2.94  | 1.15 | 1.13 |  1.61  |
| 6  | 0.64 | 0.55 | 0.54 |  1.19  | 1.21 | 1.19 |  1.91  |
| 7  | 0.76 | 0.58 | 0.61 |  3.59  | 1.28 | 1.26 |  1.91  |
| 8  | 0.88 | 0.67 | 0.66 |  0.91  | 1.36 | 1.33 |  2.1   |
+----+------+------+------+--------+------+------+--------+
```  
The following notation is introduced in this table: Tw is the system time step number, p is the measured pulse, v is the measured speed, va is the exact value of the speed, v, err% is the relative error of the speed measurement in%, E is the measured energy, Ea is the exact energy value, E, err% - relative error of energy measurement in %.  
Plot of the dependence of speed on momentum are shown in Fig. 2.  
![Fig2](Fig3-3-2.png)  
Figure 2. Velocity as function from momentum  
  
Points are measurement data, a continuous line is an analytical curved. Dash line is numerical solution (Euler method). For clarity, a plot of the dependence of speed on momentum for the classical case is also given (straight line).  
Plot of the dependence of energy on momentum are shown in Fig. 3.  
![Fig3](Fig3-3-3.png)  
Figure 3. Energy as function from momentum  
  
Points are measurement data. Dash line is numerical solution (Euler method). The continuous line is an analytical curved and compute on formule (see operation engCalculation of class mms.ResacherInstruments.DataProcessing)
  
$$
\begin{align*}  
E = \sqrt{m^2c^2 + p^2c^2 }   \\  
\end{align*}  
$$   
  
  
## 3. Description of experiment3 modul

### Class "simpleIteraction"
Description: the class is a simulation model  
Bases: mms.Composite    
`def __init__(self, sizeTick, countTick, particle_velosety, observer)`  
  
Name | Type | Description  
---- | ---- | ----------- 
sizeTick | int | size of time tact
countTick | int | count of tacts
particle_velosety | int | inicial speed particle
observer | Table instance | Detector and recorder
  
#### Operations: 
def interaction(self, car)  
Description:  action of electric field  
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

#### Attributes: 
  
Name | Type | Description  
---- | ---- | ----------- 
xAtrack | int array | x, analitical solution  
xNtrack | int array| x, numerical solution 
pA | int array| momentum, analitical solution  
vA | int array| velocity, analitical solution  
vN | int array| velocity, numerical solution
eN | int array| energy, numerical solution
  
  
#### Operations: 
**def anlSolution(self)**  
Description: accurate x (analytical formula)  
Parameters: None  
  
Algorithm: 
  
$$
\begin{align*} 
x = \frac{mc^2}{qE} \Big( \sqrt{ 1 + (\frac{qEt}{mc})^2 } -1 \Big)  \\  
v = c \sqrt{\frac{(qEt/mc)^2}{1+(qEt/mc)^2} }   \\  
\end{align*} 
$$  
  
References: Charles Kittel, Walter D.Knight, Malvin A. Ruderman, Mechanics. Berkeley physics course. Vol.1, McGraw-Hill book company. 1965  
  
**def numSolution(self)**  
Description: numerical solution of motion differential equation  (Euler method)   
Parameters: None  
  
Algorithm: 
  
$$
\begin{equation}  
p_{i} = p_{i-1} + qE \Delta t \\  
v_{i} = \frac{p_{i}} {\sqrt{m^2 + \frac{p_{i}^2}{c^2} } }\\  
x_{i} = x_{i-1} + v_{i} \Delta t  \\  
e_{i} = e_{i-1} + qE \Delta x \\  
\end{equation}  
$$  
  
where \\(p_{0} = 0\\), \\(v_{0} = 0\\),  \\(e_{0} = mc^2\\).  
  
Value \\(x_{i}\\) write to array *xNtrack*, value \\(v_{i}\\) write to array *vN*, value \\(e_{i}\\) write to array *eN*.  
    

    
