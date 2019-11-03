title: 'Implementation of the non-numeric space-time model with the Minkovsky metric'
tags:
  - UML
  - UML-profile
  - object-oriented
  - simulation
  - ontology
  - special relativity theory
authors:
  - name: Vasyliy I. Gurianov
    orcid: 0000-0003-2667-4241
    affiliation: "1"
affiliations:
 - name: SpGEU
   index: 1
date: 13 April 2019
bibliography: paper.bib

Summary

Now, simulation models are widely used in logistics, healthcare, technology, and much other areas. However, in scientific research, preference is given to numerical modeling.

The reason for this is as follows. In simulation modeling, conceptual models describe as formalism DES[1] or as ontologies, for example, on ontoUML[2,3]. It is non-numerical modeling.  
If we will use simulation, for example, in nanotechnology then we must be able to simulate of relativistic and quantum effects, and it is't clear. There is no clear understanding of how to build such simulation models.  

Here, we introduce MMS, an implementation on Python of simulation model of spacetime for the special relativity theory. This package  is intended to demonstration of possible of relativistic effect simulation. The package also demonstration production numerical data from non-numerical model. All numerical results is result of measurement on data structurs.

We used Python on two reasons. First, the Python is object-orientred languge and it is can use ontology. Second, the Python is interpretation language and it is do flexy change code.In documentation, we present package API.

We propose simulation model of spacetime as the discrete model of physical space. The simulation model described as ontology. A detailed description of this model can be found in the documentation. We use the UML2 SP [4,5]. The UML2 SP (UML Scientific Profile)  used to development of simulation model. The UML2 SP is an obect-orientired simulation lenguage and used in scientific area. It is a profile of UML. UML2 SP models are do not depend on the programming language.
In documentation, we present description two experiments. The experiments demonstration the time dilation and dynamic relativistic effects. 

References
Zeigler, B. P., H. Praehofer, and T. G. Kim. 2000. Theory of Modeling and Simulation. 2nd ed. Orlando,FL, USA: Academic Press.

1. Guizzardi, G. 2005. Ontological foundations for structural conceptual models. PhD thesis, University of 
Twente, Enschede, The Netherlands. CTIT Ph.D.-thesis series No. 05-74 ISBN 90-75176-81-3.
2. https://ontouml.org/
3. Gurianov V.I. Metamodel of simulation language UML2 SP //The Seven All-Russia Scientific-Practical Conference on Simulation and its Application in Science and Industry «Simulation. The Theory and Practice» («IMMOD-2015»), Moscow, 21-23 October, 2015.  Vol. 1. M.: IPU RAN, 2015. P.59-62. (In Russian)
4. https://vgurianov.github.io/uml-sp/
