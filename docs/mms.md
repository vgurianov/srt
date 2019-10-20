# mms.mms module
Description: modul is definition of base classes  
  
Modul use packedgs:
- import math
  
  
## class Carrier  (<<Ontological Atom>>)  
Description: User type
Concept: class is the interaction carrier  
Bases: object    
### Attributes:  
  
Name | Type | Description  
---- | ---- | ----------- 
direction | enumeration | direction in space


## class Jump:
Description: Linked list node
Concept: class is the motion count  
Bases: object    
### Attributes:  
  
Name | Type | Description  
---- | ---- | ----------- 
direction | enumeration | direction in space
next | Inctance of class Jump | next node
  
## class Leaf  (<<Ontological Atom>>)  
Description: Leaf of pattern *Composite*
Concept: a particle model 
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
Description: list *Jump* isn't *None* check  
**def jumpp(self)**  
Description: shift list *Jump*  
**def run(self)**  
Description: shift list *tmp*  
**def reset(self)**  
Description: set list *Jump* in start   
**def doImpact(self, car)**  
Description: create node *Jump* and append in list   
Parameters:  
  
Name | Type | Description  
---- | ---- | ----------- 
car | Inctance of class Carrier | interaction carrier   
  

## class Temp  
Description: Linked list *tmp* node
Concept: the moments of time   
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

## class ListItem (<<Ontological Space>>)
Description: Linked list *lst* node 
Concept: a cell of physical space  
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
Description: append new node to linked list *tmp*  
Parameters:  
  
Name | Type | Description  
---- | ---- | ----------- 
tm | Inctance of class Temp | current time moment  
  
**def ItemRun(self, tt, tGlob, c)**  
Description: activity in physical cell
Parameters:  
  
Name | Type | Description  
---- | ---- | ----------- 
tt | Inctance of class Temp | current time moment  
tGlob | int | current tick   
c | Inctance of class Carrier | interaction carrier   
  
**def resetTmp(self)**  
Description: set list *tmp* in start   
    
    
## class Composite  (<<Ontological Category>>)
Description: Composite of pattern *Composite*
Concept: a physical space model 
Bases: object    

` def __init__(self, sizeTick, countTick, observer)`  
  
Name | Type | Description  
---- | ---- | ----------- 
sizeTick | int | time tick size  
countTick | int | ticks count   
observer | Inctance of class Table | detector   
  
### Attributes:  
  
Name | Type | Description  
---- | ---- | ----------- 
tmp | Inctance of class Temp | time (list)  
lst | Inctance of class ListItem | space (list)   
carr | Inctance of class Carrier | interaction carrier  
tick | int | counter time  

### Operations:    
**def moveReset(self)**  
Description: all particles set list *Jump* in start   
**def interaction(self, carIn)**  
Description: interaction with  infinite mass 
**def run(self)**  (<<Exist>>)
Description: activity run
Concept: activity in physical space  


