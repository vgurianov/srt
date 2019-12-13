# Inertial reference frame
Modul mms.experiment3 simulate uniform translatory motion of a reference frame.  
Principle of relativity is the independence of physical laws  from the choice of inertial system. It especially important is the constancy of the speed of light.  
  

## 1. The Principle of Relativity  
Let *sVel* be velocity a reference frame (list), *lst* is base of space.  
Uniform translatory motion of a reference frame is implemented by the following code  
  
```
sV = self.sVel
while not (sV is None):
  self.lst = self.lst.right
  sV = sV.next
```  
  
Parameters:  
countTick= 8 sizeTick= 10  
Particle_velocity= 0 ,i.e beta = v/c = 0.0  
Frame_velocity= 5 ,i.e beta = v/c = 0.5  
Time count = 80  
  
```  
Uniform translatory motion of the reference frame
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
Let *frame_velocity* be velocity a reference frame, *sizeTick* is size tact of time. 
The speed limit is implemented by the following code  
  
```
        #Frame velocity
        if self.frame_velocity<=0:
            self.sVel = None
        else:
            if sizeTick - self.frame_velocity < 0:
                print "Warning: frame_velocity > sizeTick" 
            self.sVel = Jump()
            sV = self.sVel
            for i in range(1,sizeTick - self.frame_velocity):
                sV.next = Jump()
                sV = sV.next

```  
The list length *sVel* can't be more then the magnitude *sizeTick*.  
  

## 3. Description of experiment3 modul
  
### Class "irfMotion"  
  
It is class like  class freeMotion (see Experiment1.py) but has new argument frame_velocity  
and one has base class mmsEx.Composite.   
  
Description: the class is a simulation model  
Bases: mmsEx.Composite   
`def __init__(self, sizeTick, countTick, particle_velosety, observer, frame_velocity)`  
  
Name | Type | Description  
---- | ---- | ----------- 
sizeTick | int | size of time tact
countTick | int | count of tacts
particle_velosety | int | inicial speed particle
observer | Table instance | Detector and recorder
frame_velocity | int | frame velocity


### Class "mmsEx.Composite"  
It is class like  class mms.Composit (see mms.py) but has new argument frame_vel.   
`def __init__(self, sizeTick, countTick, observer, frame_vel)`  
  
Name | Type | Description  
---- | ---- | ----------- 
sizeTick | int | time tick size  
countTick | int | ticks count   
observer | Inctance of class Table | detector   
frame_vel | int | frame velocity  
  
Here changed the rule of marking.  
Let *V* be velocity a reference frame then formula \\( ct = \sqrt{s^2 + (Vs -x)^2} \\) define the new rule of marking.  
  
### New Attributes:  
  
Name | Type | Description  
---- | ---- | ----------- 
sTick | Inctance of class Temp | size tact (list) 
sVel | Inctance of class Jump | frame velocity (list) 
frame_velocity | int | frame velocity (magnitude)  
  
### Modified Operations:    
**def run(self)**  (<<Exist>>)  
It is added shift base of space (variable *lst*)   

