[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-270/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
   
# MMS: The Minkowski Metric Simulation

Now, simulation models are widely used in logistics, healthcare, technology, and much other areas. However, in scientific research, preference is given to numerical modeling.  
  
The reason for this is as follows. In simulation modeling, conceptual models describe as formalism DEVS or as ontologies, for example, on ontoUML. It is non-numerical modeling.  
If we will use simulation, for example, in nanotechnology then we must be able to simulate of relativistic and quantum effects, and it is't clear. There is no clear understanding of how to build such simulation models.  
  
Here, we introduce MMS, an implementation on Python of simulation model of spacetime for the special relativity theory. This package  is intended to demonstration of possible of relativistic effect simulation. The package also demonstration production numerical data from non-numerical model. All numerical results is result of measurement on data structurs.  
  
We used Python on two reasons. First, the Python is object-orientred language and it is can use ontology. Second, the Python is interpretation language and it is do flexy change code.In documentation, we present package API.  
  
We propose simulation model of spacetime as the discrete model of physical space. The simulation model described as ontology. A detailed description of this model can be found in the [documentation](https://vgurianov.github.io/srt/). We use the [UML2 SP](https://vgurianov.github.io/uml-sp/). The UML2 SP (UML Scientific Profile)  used to development of simulation model. It is a profile of UML. UML2 SP models are do not depend from programming languages.  
In documentation, we present description some experiments. Experiments demonstrating the time dilation and dynamic relativistic effects.  
  
## Installation  
Currently, only Python 2.7 is supported.  
  
The following dependency is required to install  
  
[matplotlib](https://matplotlib.org/) (>= 1.4)   
  
for module drawing.py.  
  
   
If you has matplotlib then install MMS from source:
  
$ git clone https://github.com/vgurianov/srt.git   
or Download ZIP.  
  
Take the package *pymms* and files from the *experiments* directory  
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
  
cd src  
python experiment1.py  ,etc.   
  
or in IDLE.  
  
Also you may install MMS from PyPI, see [Getting Started](https://vgurianov.github.io/srt/started.html).  

## Publication
Gurianov V.I. Direct measurement procedure of particle energy-momentum in model of the discrete space-time // Mathematical models and their applications: Sat. sci. tr. Issue. 21. - Cheboksary: Publishing house Chuvash. Univ., 2019. - P. 62-67.  
E-mail: vg2007sns@rambler.ru  
  

