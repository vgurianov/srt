# resacher_instruments module
This module contains classes to measurement and data processing.  
Description:
  - class *Table* is model of detector and data recorder
  - class *DataProcessing* is a processor of data.  
  
## Class "Table"
Description: class *Table* is a data recorder  
Bases: object    
`def __init__(self)`  

### Attributes: 

Name | Type | Description  
---- | ---- | ----------- 
obtG | int | array of time in the rest frame
obt | int | array of local time of cell, refined time obtG
obx | int | array of particle location
localT | int | array of local time of cell
particleT | int | array of particle time

### Operations:  
**def fixIt(self, tG, tt, xx, locT, prtT)**  
Description: Operation of write data about time and location  
Parameters:  

Name | Type | Description  
---- | ---- | ----------- 
tG | int | moment of time in the rest frame
tt | int | moment of local time of cell, refined time obtG
xx | int | particle location
locT | int | moment of local time of cell
prtT | int | moment of particle time
pulseT | int | count of interaction acts
Return: None

**detect(self, tG, c)**  
Description: Operation write data about intaraction  
Parameters:

Name | Type | Description  
---- | ---- | ----------- 
tG | int | time in the rest frame
c | Currer instance| Currer intaraction

Return: None

## Class "DataProcessing"
Description: class *DataProcessing* is a processor of data  
Bases: object    
`def __init__(self, ob, v, st, ct)` 

Name | Type | Description  
---- | ---- | ----------- 
ob | Table instance | primary data table
v | int | initial velocity of particle
st | int | size tick of time
ct | int | count tick of time

### Attributes: 

Name | Type | Description  
---- | ---- | ----------- 
obs | Table instance | primary data table
particle_velosety | int | initial velocity of particle
sizeTick | int | size tick of time
countTick | int | count tick of time
mass | int | mass = 1.0, mass of particle
lightVel | int | lightVel = 1.0 # light velocity
nu_t | int | time coefficient of conversion
nu_x | int | length coefficient of conversion
nu_m | int | mass coefficient of conversion
x | float | array of particle location
t| float | array of time moments
t_err | int | time measurement error
t_acc | float | accurate time
t_local_err | int | local error of time
vel_t | int | experimental value of velocity
vel_t_err | int | experimental error measurement
velAnl | int | alytical velocity as function from momentum
momentum_t | int | momentum of particle
eng_t_acc | int | accurate energy
eng_t | int | measurement energy
eng_t_err | int | energy measurement error


### Operations: 
**def baseCalculate(self)**  
Description: This operation call all operations from bottom. It is obligatory calculation.   
Parameters: None  
We will use International System of Units (SI) ([m], [s], [kg]).   
Time we will measurement in unit 1[m]/c[m/s] (light seconds), where c is the speed of light.

**def xtCalculate(self)**  
Description: Operation calculate t and x in SI   
Parameters: None  
  
Algorithm:  
Let \\(\tau\\) be the variable value *tt* (class *Table*), i.e. the measurement data.  
Let \\(\rho\\) be the variable value *xx* (class *Table*). It is location particle in moment tt.  
Then time \\(t\\) and coordinate \\(x\\) calculate as  
  
$$
\begin{align*}
t = \frac{\tau}{\nu_{t}} \\
x = \frac{\rho}{\nu_{x}} \\
\end{align*}
$$  
  
where \\(\nu_{t}\\) is the variable value *nu_t*, \\(\nu_{x}\\) is the variable value *nu_x*,  
t and x write to arrays *t* and *x* (class *DataProcessing*).  
Further, we will assume that \\(\nu_{t}\\) = sizeTick and \\(\nu_{x}\\) = \\(\nu_{t}\\).  
     
Example:  
If sizeTick = 10 then \\(\nu_{t}\\) = 10 and \\(\nu_{x}\\) = 10
For moment \\(\tau\\) = 10, t = 1 unit time (1/c second).  
If particle in cell \\(\rho\\) = 10 then particle coordinate is 1 [m].


**def xtAccurate(self)**  
Description: accurate t (analytical formula)  
Parameters: None  
  
Algorithm:  
Let s be the variable value *tG* (class *Table*). It is an invariant interval.  
Then 

$$
\begin{align*} 
t_{a} = \sqrt{s^2 + x^2}  
\end{align*}  
$$  
  
\\(t_{a}\\) write to array *t_acc* (class *DataProcessing*).  
  
Value \\(t_{a}\\) compare with t  
  
$$
\begin{align*} 
\epsilon =  \begin{vmatrix} \frac{t_{a} - t}{t_{a}} \end{vmatrix} \times 100 %
\end{align*}  
$$ 
  
Value \\(\epsilon\\) write to array *t_local_err*. 

**def velocityCalculate(self)**  
Description: experimental value of velocity  
Parameters: None

Algorithm:  
Let \\(v_{i}\\) be the particle velocity in moment tG and  
let \\(v_{0}\\) be the variable value *particle_velosety* (initial velocity of particle)  
then 

$$
\begin{equation}
v_{i} = \frac{\nu_{t}}{\nu_{x}} \frac{\rho_{i} - \rho_{i-1}}{\tau_{i} - \tau_{i-1}} \\
\end{equation}  
$$  
  
Value \\(v_{i}\\) write to array *vel_t*  
   
**def velErrorCalculate(self, dt, dx)**  
Description: experimental error of velocity  measurement  
Parameters:

Name | Type | Description  
---- | ---- | ----------- 
dt | float | time change (in SI)  
dx | float| change of coordinate (in SI)  
  
  
Algorithm:  
In general case, coefficient \\(\nu_{t}\\) = k*sizeTick, where k is positive integer if you need high accuracy.  
Further, we will assume that \\(\nu_{t}\\) = sizeTick and \\(\nu_{x}\\) = \\(\nu_{t}\\).  
Then absolute measurement errors are \\(\Delta t = \frac{1}{2} \frac{1}{sizeTick}\\) and \\(\Delta x = \Delta t\\).  
Let \\(\Delta v\\) be the absolute measurement error of particle velocity v.   
Then 

$$
\begin{align*} 
\Delta v &= \sqrt{ (\frac{\partial v}{\partial x_{i}} \Delta x_{i})^2 + (\frac{\partial v}{\partial x_{i-1}} \Delta x_{i-1})^2 + (\frac{\partial v}{\partial t_{i}} \Delta t_{i})^2 + (\frac{\partial v}{\partial t_{i-1}} \Delta t_{i-1})^2 } \\
&= \sqrt{2} \sqrt{ (\frac{\partial v}{\partial x} \Delta x)^2 + (\frac{\partial v}{\partial t} \Delta t)^2 }
\end{align*} 
$$  
where   
$$
\begin{align*} 
\frac{\partial v}{\partial x} = \frac{1}{dt} \\  
\frac{\partial v}{\partial t} = \frac{1}{dt} \frac{dx}{dt} \\  
\end{align*} 
$$  
  
Value \\(\Delta v\\) write to array *vel_t_err*. 
  
**def momentumCalculate(self)**  
Description: calculate particle momentum  
Parameters: None  
  
Algorithm:  
Let \\(\iota_{i} \\) be the variable value *pulseT*. It is count of interaction acts in moment tG (interaction intensity). Interaction \\(\iota_{i} \\) change list *Jump* and, сonsequently, particle velocity.   
From  
  
$$
\begin{align*}  
p = \int_0^t f \mathrm{d}t \equiv \sum_{i=0}^{tG} f_{i} \Delta t = \frac{1}{\nu_{m}} \frac{\nu_{t}}{\nu_{x}}  \sum_{i=0}^{tG} \iota_{i}
\end{align*} 
$$  
  
, i.e.  
  
$$
\begin{align*} 
p_{i+1} = p_{i} + \frac{1}{\nu_{m}} \frac{\nu_{t}}{\nu_{x}} \iota_{i} \\  
\end{align*} 
$$  
  
Value \\(p_{i}\\) write to array *momentum_t*.  
  
  
**def velAnalytical(self, p)**  
Description: velocity as function from momentum   
Parameters: p is the calculated momentum of particle  
  
Algorithm:  
Let \\(v_{a} \\) be the analitic velocite of particle.     
From  
  
$$
\begin{align*} 
p = \frac{m__{0} v}{\sqrt{1+\frac{v^2}{c^2} } }  \\
\end{align*} 
$$  
follows   
   
$$
\begin{align*} 
v = \frac{p}{\sqrt{m_{0}+\frac{p^2}{c^2} } }  \\ 
\end{align*} 
$$   
  
Value v write to array *velAnl*.  
  
**def energeAccurate(self)**  
Description: analytical accurate energy calculated   
Parameters: 

**def energeCalculate(self)**  
Description: analytical energy calculated   
Parameters: 


