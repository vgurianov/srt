# Principle of relativity
Modul mms.experiment3 simulate uniform translatory motion of a reference frame.  
Principle of relativity is the independence of physical laws  from the choice of inertial system. It especially important is the constancy of the speed of light.  
  

## 1. The Principle of Relativity
Let \\( V \\) be velocity a reference frame.  
Parameters of experiment: 
countTick= 8 sizeTick= 10  
Particle_velocity= 0 ,i.e beta = v/c = 0.0  
Time count = 80  
The reference frame velocity = 5  
  
```  
Trajectory of particle and time particle
+----+-----+-----+------+------+-----+
| Tw |  x  |  t  |  ta  | err% |  tp |
+----+-----+-----+------+------+-----+
| 0  | 0.0 | 0.0 | 0.0  | 0.0  | 0.0 |
| 1  | 0.5 | 1.2 | 1.12 | 7.33 | 1.0 |
| 2  | 1.0 | 2.3 | 2.24 | 2.86 | 2.0 |
| 3  | 1.5 | 3.4 | 3.35 | 1.37 | 3.0 |
| 4  | 2.0 | 4.5 | 4.47 | 0.62 | 4.0 |
| 5  | 2.5 | 5.6 | 5.59 | 0.18 | 5.0 |
| 6  | 3.0 | 6.8 | 6.71 | 1.37 | 6.0 |
| 7  | 3.5 | 7.9 | 7.83 | 0.94 | 7.0 |
+----+-----+-----+------+------+-----+  
```  
  
We compare with Experimen1 result  

```
Trajectory of particle and time particle
+----+-----+-----+------+------+-----+
| Tw |  x  |  t  |  ta  | err% |  tp |
+----+-----+-----+------+------+-----+
| 0  | 0.0 | 0.0 | 0.0  | 0.0  | 0.0 |
| 1  | 0.5 | 1.2 | 1.12 | 7.33 | 1.0 |
| 2  | 1.0 | 2.3 | 2.24 | 2.86 | 2.0 |
| 3  | 1.5 | 3.4 | 3.35 | 1.37 | 3.0 |
| 4  | 2.0 | 4.5 | 4.47 | 0.62 | 4.0 |
| 5  | 2.5 | 5.6 | 5.59 | 0.18 | 5.0 |
| 6  | 3.0 | 6.8 | 6.71 | 1.37 | 6.0 |
| 7  | 3.5 | 7.9 | 7.83 | 0.94 | 7.0 |
+----+-----+-----+------+------+-----+  
```  
We see that the results are identical.


## 2. The Principle of Invariant Light Speed  
  
  
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
