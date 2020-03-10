# Getting Started  
Currently, only Python 2.7 is supported. 
  
## Dependencies  
   
The following dependency is required to install and use PyMMS:  
  
[matplotlib](https://matplotlib.org/) (>= 1.4)  
for module drawing.py.  
  
## Installation

### 1. Installation to a directory
This package is intended to demonstration of the simulation code and we recommendation simple install in some directory.  
If you has matplotlib then install PyMMS from source:
  
```$ git clone https://github.com/vgurianov/srt.git```   
or Download ZIP.  
  
You must take the package *pymms* and files from the *experiments* directory and make directory  
```
src/
   ├──+pymms/  
   │      └── ... modules ...  
   │
   ├── experiment1.py  
   ├── experiment2.py  
   └── experiment3.py  
```  

You can executed experiments, for example, in command line  
```  
$cd src  
$python experiment1.py  ,and etc.   
```  
or in IDLE.  

 
### 2. Use pip to install  
Also you may install PyMMS from PyPI then dependencies install is automatic. About *pip* see [hear](https://packaging.python.org/tutorials/installing-packages/).    
Install PyMMS with pip:  
  
```$ pip install pymms```
  
or from source:  
  
```  
$ git clone https://github.com/vgurianov/srt/mms
$ cd pymms
$ pip install  
```  
  
You can find package in directory ...\Python27\Lib\site-packages  
  
Usege command  
 
```$ python -m pip show pymms```

for more information.  
  
 
  
