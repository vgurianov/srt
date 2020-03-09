# Getting Started  
Currently, only Python 2.7 is supported. 
  
## Dependencies  
   
The following dependencies are required to install and use mms:  
  
[matplotlib](https://matplotlib.org/) (>= 1.4) for module drawing.py.  
  
## Installation

### 1. Installation to a directory
This package is intended to demonstration of possible of relativistic effect simulation and we recommendation simle install in some directory.   
If you has matplotlib then install MMS from source:
  
```$ git clone https://github.com/vgurianov/srt.git```   
or Download ZIP.  
  
You must take the package *pymms* and files from the *experiments* directory.  
You must make directory  
```
[SRC]
   ├──+\pymms  
   │      └── ... modules ...  
   │
   ├── experiment1.py  
   ├── experiment2.py  
   └── experiment3.py  
```  

You can executed experiments, for example, in command line  
```  
$cd src  
$python experiment1.py  ,etc.   
```  
or in IDLE.  

 
### 2. Use pip to install  
Also you may install MMS from PyPI   
Install pymms with pip::  
  
```$ pip install pymms```
  
or from source:  
  
```  
$ git clone https://github.com/vgurianov/srt/mms
$ cd pymms
$ pip install or $ python setup.py install
```  
  
You can find modules in directory ...\Python27\Lib\site-packages  
Usege command  
 
```$ python -m pip show pymms```

for more information.  
  
About *pip* see [hear](https://packaging.python.org/tutorials/installing-packages/)  
  
