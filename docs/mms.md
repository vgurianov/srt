# mms.mms module
Description: modul is definition of base classes  
  
Modul use packedgs:
- import math
  
  
### Operations:  

## class Carrier  
Description: class is the interaction carrier  
Bases: object    
### Attributes:  
  
Name | Type | Description  
---- | ---- | ----------- 
direction | enumeration | direction in space


## class Jump:
Description: class is the motion count  
Bases: object    
### Attributes:  
  
Name | Type | Description  
---- | ---- | ----------- 
direction | enumeration | direction in space
next | Inctance of class Jump | next node
  
## class Leaf  
Description: class is the particle  
Bases: object    
`def __init__(self, v)`
  
Name | Type | Description  
---- | ---- | ----------- 
v | int | velocity of particle

### Attributes:  
  
Name | Type | Description  
---- | ---- | ----------- 
headOfJump | Inctance of class Jump | list head
currentOfJump | Inctance of class Jump | current node of list
tick | int | time counter  
  
### Operations:  

**def isActivity(self)**  
Description: operation is the  
**def jumpp(self)**  
Description: operation is the  
**def run(self)**  
Description: operation is the  
**def reset(self)**  
Description: operation is the  
**def doImpact(self, car)**  
Description: operation is the  
**def interaction(self,car)**  
Description: operation is the  

## class Temp  
Description: class is the particle  
Bases: object    
   
`def __init__(self, t)`
Name | Type | Description  
---- | ---- | ----------- 
t | Inctance of class Temp | time stamp for measurement  
  
### Attributes:  
  
Name | Type | Description  
---- | ---- | ----------- 
next | Inctance of class Temp | next node  
t | int | time counter  
marked  | Inctance of class Time | time marked  
lb | bool | time counter  

## class ListItem:
Description: class is the cell of space  
Bases: object    

`def __init__(self, x, o)`  
  
Name | Type | Description  
---- | ---- | ----------- 
x | int | coordinate stamp for measurement
o | Inctance of class Table | detector  
  
### Attributes:  
  
Name | Type | Description  
---- | ---- | ----------- 
x | int | coordinate stamp for measurement
left | Inctance of class ListItem | next node
right| Inctance of class ListItem | next node
contents| Inctance of class Leaf | content of cell
tmp| Inctance of class Time | current node of list 
temp | Inctance of class Time | head of list
observer | Inctance of class Table | detector
  
### Operations:    
**def appTemp(self, tm)**  
Description: operation is the  
**def ItemRun(self, tt, tGlob, c)**  
Description: operation is the  
**def resetTmp(self)**  
Description: operation is the  
    
    
## class Composite
Description: class is the cell of space  
Bases: object    

` def __init__(self, sizeTick, countTick, observer)`  
  
Name | Type | Description  
---- | ---- | ----------- 
sizeTick | int | size Tick of time  
sizeTick | int | detector  
observer | Inctance of class Table | detector   
  
### Attributes:  
  
Name | Type | Description  
---- | ---- | ----------- 
tmp | int | time  
lst | int | space  
carr | int | interaction carrier  
tick | int | counter time  

### Operations:    
**def move(self)**  
Description: operation is the  
**def interaction(self, carIn)**  
Description: operation is the  
**def run(self)**  
Description: operation is the  


