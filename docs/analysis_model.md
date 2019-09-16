# Analysis model
In UML2 SP, simulation model described as ontology. Classes are considered as the Minsky frames. The language details  view on site  [https://vgurianov.github.io/uml-sp/](https://vgurianov.github.io/uml-sp/)  
  
## 1. Ontology of Special Relativity Theory  
Semantic net definition.  
Classical mechanics concepts can view on [page](https://vgurianov.github.io/uml-sp/case_studies/newton/newton).  
In relativistic mechanics, concepts similar concepts of classical mechanics but there are differences. It is synchronization rule of  time of mechanical system and local time of cells.  
Main concepts are Mechanical system, Cell of space, Moment of time, Local Time, and Synchronization (fig.1). 
  
![Fig1](Fig1-2-1.png)
Figure 1. Ontology of Special Relativity Theory   
  
Also, see  
[Full diagram](Fig1-2-1a.png)  
[Pseudo code C++](cpp.md)  

## 2. Realization of use case "Run"
Use case "Run" realization is depicted in Fig.2.  
![Fig2](Fig1-2-2.png)  
Figure 2. Communication diagram of operation "Run"  

## 3. Spacetime model  
We propose a following model of Minkowski spacetime (Fig.3).  
"Composite" class is a model of a physical spacetime. We will view one-dimension space. Physical space is linked list, where lst attribute is base of space (In general case, "headOfList" attribute is base of space, and "tailOfList" is the anchor point and specify the direction in the physical space). Attribute "tmp" is one-direction linked list and it is a model of physical time. Attribute "tmp" is instance of class Temp.  
Class "ListItem" is model of a physical space cell. The cell has a local time; it is "tmp" attribute.  
The time of "Composite" class and the time "ListItem" class must be synchronization.   
![Fig3](Fig1-2-3.png)
Figure 3. Minkowski spacetime model

The synchronization mechanism is a following process. Operation "Run" of class Composite has cycle by linked list "temp". For each t node of linked list (system tick) sended message runItem(t) to all cells of space (Fig.2). 
![Fig4](Fig1-2-4.png)
Figure 4. 	Communication process of synchronization


In operation runItem(t), t compared with attribute "marked" of current node of "temp" (lt on Fig2). If t equals "marked" then linked list "temp" of ListItem shift to next node (operation nextTemp() on Fig2). This is jump (tick) of local time of cell. If cell has the particle then time of particle also make tick (operation Run() on Fig2).

	void ItemRun(Temp *tt, int tGlob, Carrier *c) {
		if (tmp != NULL) {
			if (tt == tmp->marked) {
				if (contents != NULL) {
					contents->Run();   // exist of particle
					observer->fixIt(tGlob, tt->t, x, tt->t, contents->tick);  						contents->doImpact(c); // interaction
					observer.detect(tGlob,c); // observe act of interaction
				};
			tmp = tmp->next;  // time run in cell
			};
		};
    }
    
Both Newton's time and time of special relativity has same synchronization mechanism but different rule of define "marked" label. In Newton's mechanics, the time of "Composite" class and the time "ListItem" class have same lengths of linked list "temp" and label "marked" has same number with number of node "temp". For example, for node number one of "temp", all cells of space has label "one" in attribute "marked" and all cells do one tick at the same time.
Time of special relativity has following rule. We take more details grid, let is be 100 x 100 grid (rs=100) of time-space. Each ten node is marked as lb = true; it is "bearing" node. Further, cells mark as


	Temp *tt; ListItem *ll; int s; Temp *st;
	tt = tmp;
	while (tt != NULL) {
		if (tt->lb) { // It is moment of time
			ll = lst;
			while (ll != NULL) {
				s = sqrt(tt->t*tt->t +ll->x*ll->x); //ceil,floor
				if (s<size) {
					  st = tmp;
					  for (int i = 0; i < s; i++) st = st->next;
					  ll->appTemp(st);
				};
			ll = ll->right;
			};
		};
	tt = tt->next;
	};
	
i.e. used formula is  \\( s^2 = c^2t^2 - x^2  \\).  
The operation appTemp(tm) create new node of type Temp in cell and mark it as tm.
![Fig5](Fig1-2-5.png)  
Figure 5. 	Example of linked list tmp for cells 20 and 80  



## 4. Mechanical motion  and interaction
Both mechanical motion and interaction models in SRT as in classical methanic.  
Mechanical motion is depicted in fig.6.   
![Fig6](Fig1-2-6.png)  
Figure 6. 	Mechanical motion  
  
Interaction  
 

## 5. Measurements
All epistemology entities has standard types (int, bool, and itc.).  
We define the unprimed system foolow.  
- Space cells marked numbers from 0 to Nmax. It is variable x class ItemList.  
- Time interval marked number from 0 to Nmax. It is variable t class Temp.  
- Counter of bearing (abutting) node (lb = true) is variable "tick". 
- In all cells put detector of location and interaction. It is variable "observer" of class Table.  
  
We define time of particle (the primed system) as variable "tick" class Component.  
  
Main measurement is account. Absolute error of measurement then is 0.5.  
Operation of measurement is depicted in Fig.7  
![Fig7](Fig1-2-7.png)  
Figure 7. 	The measurement  
  
Message fixIt() send if cell isn't empty and tt = tmp.lb. Operation fixIt() write x,t, and other variable to table.  
