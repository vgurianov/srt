---
title: 'PyMMS: Implementation of a non-numeric spacetime model with the Minkovsky metric'
tags:
  - special relativity theory
  - the Minkowski metric
  - simulation
  - ontology
  - UML
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

Today, simulation models are widely used in logistics, healthcare, technology, and other areas. However, in scientific research, there is preference for numerical modeling.
The reason for this is as follows. In simulation modeling, conceptual models are described as formalism DEVS [@Zeigler:2000] or as ontologies, for example, on ontoUML[@Guizzardi:2005]. This is non-numerical modeling.
  
If we use simulation, for example, in nanotechnology, then we must be able to simulate relativistic and quantum effects, and there is no clear understanding of how to build such simulation models.  

Here, we would like to introduce a PyMMS package, a Python implementation of a simulation model of spacetime for the special relativity theory. This package is intended for the demonstration of the possibility of simulating the relativistic effect. The package also demonstrates the production numerical data from the non-numerical model. All numerical data is a result of measurement in data structures.

We used Python for two reasons. First, Python is an object-oriented language, which makes it posible for it to use ontology. Second, Python is an interpreted language, which makes it posible to flexibly change code. We provide the package API in the documentation.

We propose a simulation model of spacetime as a discrete model of physical space. The simulation model is described as an ontology. A brief communication has been published in [@Gurianov:2019]. A detailed description of this model can be found in the documentation. We use the UML2 SP [@Gurianov:2015; @umlsp]. The UML2 SP (UML Scientific Profile)  is used for the development of simulation models. UML2 SP is an object-oriented simulation language that is used in scientific areas. It is a profile of UML. UML2 SP models do not depend on the programming language.  
We provide a description of several experiments in the documentation. The experiments demonstrate the time dilation and dynamic relativistic effects. 

# References
