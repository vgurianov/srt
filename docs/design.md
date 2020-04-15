# Design model  
  
## 1. Class diagram
The design model is made for Python. The class diagram depicted in Fig.1   

![Fig1](Fig1-3-1.png)
  
Figure 1. Class diagram  

## 2. Components
Classes are placed in four modules. Component diagram is depicted in Fig.2  
  
![Fig2](Fig1-3-3.png)  
Figure 2. Component diagram   
  
Module *mms* include Jump, Carrier, Leaf, Temp, and Composite classes.
Module *resacher_instruments*  include Table and DataProcessing classes.  
Module *print_results*  include TablePrint  class.  
Module *drawing* include Visualization class.  
  
  
## 3. Sync errors  
Error in moment Tw = 8 is  
  
```
Parameters:
countTick= 10 sizeTick= 10
Particle_velosety= 5 ,i.e beta = v/c = 0.5
Time count = 100
Particle velosety = 5

...
Tw = 7
Particle tick=: 7
ListItem is act: for tt=marked= 79 ListItem= 35 tloc= 7
Tw = 8
Tw = 9
Sync error: Particle reset but cell= 40  not sync
Particle tick=: 8
ListItem is act: for tt=marked= 92 ListItem= 45 tloc= 8

```  
The cause of the error is shown in Fig. 3  
![Fig3](Fig1-3-2.png)  
Figure 3. Sync error  
  
If particle move is ends then the time of particle is sync.  
This error appear if  \\(\sqrt{T_{w}^2+x_{i}^2} > T_{w}+1\\). In moment \\(T_{w}+1\\) has operation *resetMove()* and particle has move again. We used variable *_err_flag* to spy the error.  
This problem has a solution.  
