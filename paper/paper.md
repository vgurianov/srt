---
title: 'Implementation of the non-numeric space-time model with the Minkovsky metric'
tags:
  - special relativity theory
  - the Minkowski metric
  - simulation
  - UML
  - ontology
  - Python
authors:
  - name: Vasyliy I. Gurianov
    orcid: 0000-0003-2667-4241
    affiliation: "1"
affiliations:
 - name: Saint-Petersburg State Economic University, Branch in Cheboksary
   index: 1
date: 13 April 2020
bibliography: paper.bib
---

# Summary

Now, simulation models are widely used in logistics, healthcare, technology, and many other areas. However, in scientific research, preference is given to numerical modeling.
The reason for this is as follows. In simulation modeling, conceptual models describe as formalism DEVS [@Zeigler:2000] or as ontologies, for example, on ontoUML[@Guizzardi:2005]. It is non-numerical modeling.
  
If we will use simulation, for example, in nanotechnology then we must be able to simulate relativistic and quantum effects, and it isn't clear. There is no clear understanding of how to build such simulation models.  

Here, we introduce PyMMS, an implementation of Python of simulation model of spacetime for the special relativity theory. This package is intended to demonstrate the possibility of relativistic effect simulation. The package also demonstration production numerical data from the non-numerical model. All numerical data is a result of measurement on data structures.

We used Python for two reasons. First, the Python is an object-oriented language and it is can use ontology. Second, the Python is an interpreted language and it does flexy change code. In documentation, we present the package API.

We propose a simulation model of spacetime as the discrete model of physical space. The simulation model described as ontology. Brief communication published in [Gurianov:2019]. A detailed description of this model can be found in the documentation. We use the UML2 SP [@Gurianov:2015; @umlsp]. The UML2 SP (UML Scientific Profile)  used to development of simulation models. The UML2 SP is an object-oriented simulation language and used in scientific areas. It is a profile of UML. UML2 SP models do not depend on the programming languages.
In the documentation, we present a description of several experiments. Experiments demonstrate the time dilation and dynamic relativistic effects. 

# References
