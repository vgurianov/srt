# Design model  
  
## 1. Class diagram
Disign model make to Python. The class diagram depicted in Fig.1   

![Fig1](Fig1-3-1.png)
  
Figure 1. Class diagram  

## 2. Components
Classes are placed in four modules. Component diagram is depicted in Fig.2  
  
![Fig2](Fig1-3-3.png)  
Figure 1. Class diagram   
  
Module mms include Jump, Carrier, Leaf, Temp, and Composite classes.
Module resacher_instruments  include Table and DataProcessing classes.  
Module print_result  include TablePrint  class.  
Module graphs  include Visualization  class.  
  
  
## 3. Sync errors  
Error in moment Tg = 5  
  
```
Parameters:
countTick= 10 sizeTick= 10
Count = 100
Particle velosety = 6

World time = 4
Particle tick=: 4
ListItem is act: for tt=marked= 47 ListItem= 24 tloc= 4
World time = 5
Particle tick=: 5
ListItem is act: for tt=marked= 50 ListItem= 30 tloc= 4
,and ListItem is act: for tt=marked= 59 ListItem= 30 tloc= 5
World time = 6
Particle tick=: 6
ListItem is act: for tt=marked= 62 ListItem= 36 tloc= 5
World time = 7
Particle tick=: 7
ListItem is act: for tt=marked= 74 ListItem= 42 tloc= 6


Measurement result:
+----+----+----+-------+------+-------------+------+
| Tw | t  | x  | MarkT | prtT | Accurate t= | err% |
+----+----+----+-------+------+-------------+------+
| 0  | 0  | 0  |   0   |  0   |     0.0     | 0.0  |
| 1  | 12 | 6  |   12  |  1   |     11.7    | 2.9  |
| 2  | 24 | 12 |   24  |  2   |     23.3    | 2.9  |
| 3  | 35 | 18 |   35  |  3   |     35.0    | 0.0  |
| 4  | 47 | 24 |   47  |  4   |     46.6    | 0.8  |
| 5  | 59 | 30 |   59  |  5   |     58.3    | 1.2  |
| 6  | 62 | 36 |   62  |  6   |     70.0    | 11.4 |
| 7  | 74 | 42 |   74  |  7   |     81.6    | 9.4  |
| 8  | 85 | 48 |   85  |  8   |     93.3    | 8.9  |
| 9  | 97 | 54 |   97  |  9   |    105.0    | 7.6  |
+----+----+----+-------+------+-------------+------+```
```  
The cause of the error is shown in fig. 2
![Fig3](Fig1-3-2.png)
Figure 3. Sync error tick = 5 
  
