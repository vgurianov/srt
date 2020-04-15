# resacher_instruments module
This module contains classes for measurement and data processing.  
Description:
  - class *Table* is a model of detector and data recorder
  - class *DataProcessing* is a processor of data.  
  
## Class "Table"
Description: class *Table* is a data recorder  
Bases: object    
`def __init__(self)`  

### Attributes: 
  
Name | Type | Description  
---- | ---- | ----------- 
obt_g | int | array of time in the rest frame
obt | int | array of local time of cell, refined time obtG
obx | int | array of particle location
local_t | int | array of local time of cell
particle_t | int | array of particle time
pulse_t | int | interaction acts
 
### Operations:  
**def fix_it(self, tg, tt, xx, loc_t, prt_t)**  
Description: Operation of write data about time and location   
Parameters:  
  
Name | Type | Description  
---- | ---- | -----------  
tg | int | moment of time in the rest frame  
tt | int | moment of local time of cell, refined time obtG  
xx | int | particle location  
loc_t | int | moment of local time of cell  
prt_t | int | moment of particle time  
  
Returns: None  
  
**detect(self, tg, c)**  
Description: Operation write data about interaction  
Parameters:

Name | Type | Description  
---- | ---- | ----------- 
tg | int | time in the rest frame
c | Currer instance| Currer interaction

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
size_tick | int | size tick of time
count_tick | int | count tick of time
mass | int | mass = 1.0, mass of particle
light_vel | int | lightVel = 1.0 # light velocity
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
vel_anl | int | analytical velocity as function from momentum
momentum_t | int | momentum of particle
eng_t_acc | int | accurate energy
eng_t | int | measurement energy
eng_t_err | int | energy measurement error
eng_t_err_sum | int | energy measurement error in sum 


### Operations: 
**def base_calculate(self)**  
Description: This operation call all operations from the bottom. It is an obligatory calculation.   
Parameters: None  
We will use International System of Units (SI) ([m], [s], [kg]).   
Time we will measurement in unit 1[m]/c[m/s] (light seconds), where c is the speed of light.

**def xt_calculate(self)**  
Description: Operation calculate t and x in SI   
Parameters: None  
  
Algorithm:  
Let \\(\tau\\) be the variable value *tt* (class *Table*), i.e. the measurement data.  
Let \\(\rho\\) be the variable value *xx* (class *Table*). It is location particle in moment tt.  
Then time \\(t\\) and coordinate \\(x\\) calculate as  
  
$$
\begin{align*}
t = \frac{\tau}{\nu_{t}} ,  x = \frac{\rho}{\nu_{x}} , \\
\end{align*}
$$  
  
where \\(\nu_{t}\\) is the variable value *nu_t*, \\(\nu_{x}\\) is the variable value *nu_x*,  
t and x write to arrays *t* and *x* (class *DataProcessing*).  
Further, we will assume that \\(\nu_{t}\\) = size_tick and \\(\nu_{x}\\) = \\(\nu_{t}\\).  
     
Example:  
If size_tick = 10 then \\(\nu_{t}\\) = 10 and \\(\nu_{x}\\) = 10
For moment \\(\tau\\) = 10, t = 1 unit time (1/c second).  
If particle in cell \\(\rho\\) = 10 then particle coordinate is 1 [m].


**def xt_accurate(self)**  
Description: accurate t (analytical formula)  
Parameters: None  
  
Algorithm:  
Let s be the variable value *tg* (class *Table*). It is an invariant interval.  
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

**def velocity_calculate(self)**  
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
   
**def vel_error_calculate(self, dt, dx)**  
Description: experimental error of velocity  measurement  
Parameters:

Name | Type | Description  
---- | ---- | ----------- 
dt | float | time change (in SI)  
dx | float| change of coordinate (in SI)  
  
  
Algorithm:  
In general case, coefficient \\(\nu_{t}\\) = k*size_tick, where k is positive integer if you need high accuracy.  
Further, we will assume that \\(\nu_{t}\\) = size_tick and \\(\nu_{x}\\) = \\(\nu_{t}\\).  
Then absolute measurement errors are \\(\Delta t = \frac{1}{2} \frac{1}{sizeTick}\\) and \\(\Delta x = \Delta t\\).  
Let \\(\Delta v\\) be the absolute measurement error of particle velocity v.   
Then 

$$
\begin{align*} 
\Delta v &= \sqrt{ (\frac{\partial v}{\partial x_{i}} \Delta x_{i})^2 + (\frac{\partial v}{\partial x_{i-1}} \Delta x_{i-1})^2 + (\frac{\partial v}{\partial t_{i}} \Delta t_{i})^2 + (\frac{\partial v}{\partial t_{i-1}} \Delta t_{i-1})^2 } \\
&= \sqrt{2} \sqrt{ (\frac{\partial v}{\partial x} \Delta x)^2 + (\frac{\partial v}{\partial t} \Delta t)^2 ,}
\end{align*} 
$$  
where   
$$
\begin{align*} 
\frac{\partial v}{\partial x} = \frac{1}{dt} , \frac{\partial v}{\partial t} = \frac{1}{dt} \frac{dx}{dt} .\\  
\end{align*} 
$$  
  
Value \\(\Delta v\\) write to array *vel_t_err*. 
  
**def momentum_calculate(self)**  
Description: calculate particle momentum  
Parameters: None  
  
Algorithm:  
Let \\(\iota_{i} \\) be the variable value *pulse_t*. It is count of interaction acts in moment tg (interaction intensity). Interaction \\(\iota_{i} \\) change list *Jump* and, сonsequently, particle velocity.   
We have  
  
$$
\begin{align*}  
p = \int_0^t f \mathrm{d}t \approx \sum_{i=0}^{Tw} f_{i} \Delta t = \frac{1}{\nu_{m}} \frac{\nu_{t}}{\tau_{R}^2} \frac{\tau_{R}}{\nu_{t}} \sum_{i=0}^{Tw} \iota_{i} , \\
\end{align*} 
$$  
  
i.e.  
  
$$
\begin{align*} 
p_{i+1} = p_{i} + \frac{1}{\nu_{m}} \frac{1}{\tau_{R}} \iota_{i} \\  
\end{align*} 
$$  
  
Value \\(p_{i}\\) write to array *momentum_t*.  
  
  
**def vel_analytical(self, p)**  
Description: velocity as function from momentum   
Parameters: p is the calculated momentum of particle  
  
Algorithm:  
Using \\(p = \frac{m_{0} v}{\sqrt{1 - v^2 / c^2 } }  \\), we get \\(v = \frac{p}{\sqrt{m_{0}^2+p^2 / c^2 }}  \\).  
  
Value \\(v\\) write to array *vel_anl*.  
  
**def energe_accurate(self)**  
Description: energy as function from momentum   
Parameters: None
  
Algorithm:  
Let \\(E_{acc} \\) be the analytic energy of particle.     
We clearly have  
  
$$
\begin{align*} 
E_{acc} =  \sqrt{m_{0}^2 c^4 + p^2 c^2}  \\ 
\end{align*} 
$$  
  
Value \\(E_{acc}\\) write to array *eng_t_acc*.  
    
**def energe_calculate(self)**  
Description: measured energy calculate   
Parameters: None  
  
Algorithm:  
Let \\(E \\) be the energy of particle.     
We have  
  
$$
\begin{align*}  
E = m_{0} c^2 + \int_0^t fv \mathrm{d}t \approx m_{0} c^2 + \sum_{i=1}^{Tw} f_{i} v_{i}\Delta t ,\\  
\end{align*} 
$$  
  
i.e.  
  
$$
\begin{align*} 
E_{i+1} = E_{i} + f_{i} (x_{i} - x_{i-1}) ,\\  
\end{align*} 
$$  
  
where \\(E_{0} = m_{0} c^2\\).  
  
Value \\(E_{i}\\) write to array *eng_t*.  
  
Measure erorr is
  
$$
\begin{align*} 
\Delta E_{i} &= \sqrt{ (\frac{\partial E}{\partial x_{i}} \Delta x_{i})^2 + (\frac{\partial E}{\partial x_{i-1}} \Delta x_{i-1})^2} \\  
\end{align*} 
$$  
  
Value \\(\Delta E_{i}\\) write to array *eng_t_err*.    
  
Full measure erorr is  
  
$$
\begin{align*}  
\Delta Es_{i} =  \sqrt{\sum_{k=0}^{i} \Delta E_{k}^2} \\  
\end{align*}  
$$  
  
Value \\(Es_{i}\\) write to array *eng_t_err_sum*.    
  
