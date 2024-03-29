[![Build Status](https://travis-ci.org/vgurianov/srt.svg?branch=master)](https://travis-ci.org/vgurianov/srt) [![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-270/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
   
# PyMMS: The Minkowski Metric Simulation

Now, simulation models are widely used in logistics, healthcare, technology, and many other areas. However, in scientific research, preference is given to numerical modeling.   
  
The reason for this is as follows. In simulation modeling, conceptual models describe as formalism DEVS or as ontologies, for example, on ontoUML. It is non-numerical modeling.  
If we will use simulation, for example, in nanotechnology, then we must be able to simulate relativistic and quantum effects, and it isn't clear. There is no clear understanding of how to build such simulation models.  
  
Here, we introduce PyMMS, an implementation of Python of simulation model of spacetime for the special relativity theory. This package is intended to demonstrate the possibility of relativistic effect simulation in OOS (object-oriented simulation) and ABS (agent-based simulation). The package also demonstration production numerical data from the non-numerical model. All numerical data is a result of measurement on data structures.  
  
We used Python for two reasons. First, the Python is an object-oriented language and it is can use ontology. Second, the Python is an interpreted language and it does flexy change code.  We present the package API in the [documentation](https://vgurianov.github.io/srt/).  
  
We propose a simulation model of spacetime as a discrete model of physical space. The simulation model described as an ontology. A detailed description of this model can be found in the [documentation](https://vgurianov.github.io/srt/). This paper has relationship to the program by Stephen Wolfram [(arXiv:2004.08210)](https://arxiv.org/abs/2004.08210). We use the [UML2 SP](https://vgurianov.github.io/uml-sp/). The UML2 SP (UML Scientific Profile) used to development of simulation models. It is a profile of UML. UML2 SP models do not depend on programming languages.  
  
In the documentation, we present a description of several experiments. Experiments demonstrating the time dilation and dynamic relativistic effects.  
  
## Publication
1. Gurianov V.I. Direct measurement procedure of particle energy-momentum in model of the discrete space-time // Mathematical models and their applications: Sat. sci. tr. Issue. 21. - Cheboksary: Publishing house Chuvash. Univ., 2019. - P. 64-69.  
2. [Gurianov V.I. Simulation model of spacetime with the Minkowski metric, arXiv:2009.10689 [cs.CE], 2020](https://arxiv.org/abs/2009.10689)
  
## Getting started with PyMMS  
Currently, only Python 2.7 is supported.  
  
The following dependency is required to install  
  
[matplotlib](https://matplotlib.org/) (>= 1.4, version 2.2.4 recommended)   
  
for the module drawing.py.  
  
   
If you have matplotlib then take PyMMS from source.  
Go to https://github.com/vgurianov/srt/ and click the green button "Code", then click "Download ZIP" to download the whole repository.  
  
You must take the package *pymms* and files from the *experiments* directory.  
You must make directory  
```
src/
   ├──+pymms/  
   │      └── ... modules ...  
   │
   ├── experiment1.py  
   ├── experiment2.py  
   └── experiment3.py  
```  

You can execute experiments, for example, in the command line  
  
```
$ cd src  
$ python experiment1.py  ,and etc.   
```  
   
or in IDLE.  
  
Also, you may install PyMMS from PyPI, see [Getting Started](https://vgurianov.github.io/srt/started.html).  
  
## Contributing  
We welcome contributions to the srt repo.  
The goal of this project is to present code that is as clear as possible to understanding. We sacrifice versatility, optimality, and even error protection.  
Some suggested types of contributions include:
  
- Bug fixes  
- Documentation improvements  
- Extensions to the experiments  
  
The feedback is very welcome   
e-mail: vg2007sns@rambler.ru  

