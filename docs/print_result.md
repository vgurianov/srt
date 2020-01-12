# mms.pint_results module
Description: modul is printer of experimental data  
  
Modul use packedgs:
- from external.prettytable import PrettyTable
- import math

## class TablePrint (self, dat)  
Description: class is the data print  
Bases: object    
`def __init__(self, dat)`  
   
Name | Type | Description  
---- | ---- | ----------- 
dat | Inctance of class “DataProcessing” | experiment data  

### Attributes:  
  
Name | Type | Description  
---- | ---- | ----------- 
dt | Inctance of class “DataProcessing” | experiment data 
  
  
### Operations:  
 
**def xt_print_simple(self) and def xtPrintPrettyTable(self)**  
coordinates print  
print dt.x[i], dt.t[i], dt.t_acc[i]

**def vel_print_simple(self)**  
velocity print

**def eng_print_simple(self)**  
energy print

**def fromp_print_prettytable(self)**
velocity and energy print
  
  
# mms.drawing module  
Description: modul is builder of plots  
  
Modul use packedgs:
- import math
- import matplotlib.pyplot
- import matplotlib.ticker
- import pylab

## class Visualization  
Description: class Visualization is the data visualizator  
Bases: object    
`def __init__(self, dat)`    
   
Name | Type | Description  
---- | ---- | ----------- 
dat | Inctance of class “DataProcessing” | experiment data 

### Attributes:  
  
Name | Type | Description  
---- | ---- | ----------- 
dt | Inctance of class “DataProcessing” | experiment data 
  
  
### Operations:  
  
**def trajectory(self)**  
Description: Treck of particle  
Parameters: None  
  
**def trajectory1(self)**  
Description:  Treck and curve of invariant interval s  
Parameters: None  
      
**def v_from_p_function(self)**  
Description:  velocity plot, particle velocity as function momentum   
Parameters: None  
      
**def e_from_p_function(self)**  
Description:  energy plot, particle energy as function momentum  
Parameters: None  
    
