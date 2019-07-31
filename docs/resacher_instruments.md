# resacher_instruments module
This module contains classes to measurement and data processing.  
Description:
  - class *Table* is model of detector and data recorder
  - class *DataProcessing* is a processor of data.  
  
## Class "Table"
Description: class *Table* is a data recorder  
Bases: object    
Parameters:	None  

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
tG | int | array of time in the rest frame
tt | int | array of local time of cell, refined time obtG
xx | int | array of particle location
locT | int | array of local time of cell
prtT | int | array of particle time

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
Parameters:	ob, v, st, ct 

Name | Type | Description  
---- | ---- | ----------- 
ob | int | array of global time
v | int | array of local time of cell
st | int | array of particle location
ct | int | array of particle location

### Attributes: 

Name | Type | Description  
---- | ---- | ----------- 
obtG | int | array of global time
obt | int | array of local time of cell
obx | int | array of particle location

obs = None
    particle_velosety = None
    sizeTick = None
    countTick = None
    mass = 1.0 # mass of particle
    lightVel = 1.0 # light velocity
    nu_t = 0.0  # time coefficient of conversion
    nu_x = 0.0  # length coefficient of conversion
    nu_m = 0.0  # mass coefficient of conversion 

    x = []
    t = []
    t_err = []
    t_acc = []
    t_local_err = []
    
    vel_t = []      # experimental value of velocity
    vel_t_err = []  # experimental error measurement
    velAnl = []     # analytical velocity as function from momentum

    momentum_t = []
    eng_t_acc = []
    eng_t = []
    eng_t_err = []

### Operations: 

**def xtCalculate(self)**  
Description: Operation write data about t and x  
Parameters:  

**def xtAccurate(self)**  
Description: accurate t (analytical formula)  
Parameters: 

**def velocityCalculate(self)**  
Description: experimental value of velocity  
Parameters: 

**def velErrorCalculate(self, dt, dx)**  
Description: experimental error measurement of velocity  
Parameters: 

**def momentumCalculate(self)**  
Description: experimental error measurement of velocity  
Parameters: 

**def velAnalytical(self, p)**  
Description: analytical velocity as function from momentum   
Parameters: 

**def energeAccurate(self)**  
Description: analytical accurate energy calculated   
Parameters: 

**def energeCalculate(self)**  
Description: analytical energy calculated   
Parameters: 

**def baseCalculate(self)**  
Description: This operation call all operations from top. It is obligatory calculation.   
Parameters: None

