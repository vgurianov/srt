# Analysis model

## 1. Ontology of Special Reletivity Theory  
Semantic net definition.  
Concepts are System, Cell of space, Time of System, Local Time, and Synchronization (fig.1). 
  
![Fig2](Fig1-2-1.png)
Figure 1. Ontology of Special Reletivity Theory   
  
Also, see  
[Full diagram](Fig1-2-1a.png)  
[Pseudo code C++](http://example.net/)  


## 2. Spacetime model  
Предположение 1. Синхронизация выполняется методом «ожидания»
We propose a following model of Minkowski spacetime.  
"Composite" class is a model of a physical spacetime We will view one-dimension space. Physical space is linked list, where "headOfList" attribute is base of space, and "tailOfList" is the anchor point and specify the direction in the physical space. 
Attribute "temp" is one-direction linked list and it is a model of physical time.
Class "ListItem" is model of a physical space cell. The cell has a local time; it is "temp" attribute. The time of "Composite" class and the time "ListItem" class must be synchronization.
Procedure “Synchronization”  

Figure 3. Time synchronisation in cells of space

The synchronization mechanism is a following process. Operation "Run" of class Composite has cycle by linked list "temp". For each t node of linked list (system tick) sended message runItem(t) to all cells of space (Fig.2). 
Figure 2. 	Communication process of synchronization


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
	
i.e. used formula is  .  
The operation appTemp(tm) create new node of type Temp in cell and mark it as tm.
  
## 3. Mechanical motion  

## 4. Ineraction  

## 5. Measurements

All epistemology entities has standard types (int, bool, and itc.).

