# mms.pint_result module
Description: modul is printer of experimental data  
  
Modul use packedgs:
- from external.prettytable import PrettyTable
- import math

## class ResultsPrint (self, dat):
Description: class is the data print
Bases: object    
def __init__(self, dat)  
  
Name | Type | Description  
---- | ---- | ----------- 
dat | Inctance of class “DataProcessing” | experiment data  

### Attributes:  
  
Name | Type | Description  
---- | ---- | ----------- 
dp | Inctance of class “DataProcessing” | experiment data 
  
  
### Operations:  
 
**def xtPrintSimple(self) and def xtPrintPrettyTable(self)**  
coordinates print  
print dt.x[i], dt.t[i], dt.t_acc[i]

**def velPrintSimple(self)**  
velocity print

**def engPrintSimple(self)**  
energy print

**def frompPrintPrettyTable(self)**
velocity and energy print


# mms.graths module  
Description: modul is builder of plots  
  
Modul use packedgs:
- import math
- import matplotlib.pyplot
- import matplotlib.ticker
- import pylab

## class Visualization
Description: class Visualization is the data visualizator
Bases: object    
def __init__(self, d)  
  
Name | Type | Description  
---- | ---- | ----------- 
d | Inctance of class “DataProcessing” | experiment data 

### Attributes:  
  
Name | Type | Description  
---- | ---- | ----------- 
dp | Inctance of class “DataProcessing” | experiment data 
  
  
### Operations:  
  
**def trajectory(self)**
Description: Treck of particle
Parameters: None  

**def trajectory1(self)**
Description:  Treck and curve of invariant interval s
Parameters: None  
      
**def vFromPfunction(self)**
Description:  velocity plot, particle velocity as function momentum  
Parameters: None  
      
**def eFromPfunction(self)**
Description:  energy plot, particle energy as function momentum  
Parameters: None  
    
