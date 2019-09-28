```
//---------------------  ReusableClasses.h   -----------------

#ifndef ReusableClassesH
#define ReusableClassesH

#include <Classes.hpp>
#include <StdCtrls.hpp>
#include <Dialogs.hpp>
#include <math.h>

#include "InstrumentClasses.h"
//---------------------------------------------------------------------------
enum DirectionOption {FORWARD, BACKWARD};
// carrier of intaraction
class Carrier {
public:
DirectionOption direction;

	Carrier(){direction = FORWARD;}
	Carrier(DirectionOption d){direction = d;}

};
// resurce of motion
class Jump {
public:
	DirectionOption direction;
	Jump *next;

	Jump(DirectionOption d) {direction = d; next = NULL;}
};
//---------------------------------------------------------------------------

	/******************************************************
	 *  Class:   <<Substance>> Component
	 *  The class is Component role in Composite pattern
	 *  ***
	 *  Concept = Phisical matter
	 * ***************************************************/

class Component {
private:
protected:
public:
	int tick;  // counter of time, it is instrument

	Jump *headOfJump, *currentOfJump; // ** Concept = Resource of motion
	bool isActivity;    // ** Concept = Activity/Passivity state of matter

	Component() {
		headOfJump = NULL;  currentOfJump = headOfJump;
		tick = -1;
	}
	virtual void Run() = 0;
	// motion
	void jumpp(){
		if (currentOfJump != NULL) {
			currentOfJump = currentOfJump->next;
		} else {
		//ShowMessage(IntToStr(this->number)+" Particle Non Active");
		isActivity = false;};
	}

	// new tackt of motion
	void reset() {
	if (headOfJump != NULL) {isActivity = true; };
	currentOfJump = headOfJump;
	}
	// ** Concept = Influence, Newton's second law
	virtual void doImpact(Carrier *f) {
		if (f != NULL) {
			if (headOfJump != NULL) {
				Jump *j; j = new Jump(FORWARD);  // Attention! Only forward
				j->next = headOfJump;
				headOfJump = j;
			} else {headOfJump = new Jump(FORWARD);};
		};
	}
	// ** Concept = Influence, Newton's 3 law
	virtual void interaction(Carrier *f) {
		//if (f != NULL) {
	}

};   // class Component

	/******************************************************
	 * Class:   <<Ontology Atom>> Leaf
	 *  The class is Leaf role in Composite pattern
	 *  ***
	 *  Concept = Point particle
	 * ***************************************************/
class Leaf: public Component {
private:
protected:
public:
	Leaf() {
	}
	Leaf(int m, int v) { // m - mass (m=1), v - initial velocety >= 0
		headOfJump = NULL;
		if (v>0) {
			headOfJump = new Jump(FORWARD);
			currentOfJump = headOfJump;
			for (int i = 1; i<v; i++) {
				currentOfJump->next = new Jump(FORWARD);
				currentOfJump = currentOfJump->next;
			};
			currentOfJump = headOfJump;
			isActivity = true;
		};
		if (v<0) ShowMessage( "Velosety must be >=0; v= "+IntToStr(v));
		tick = -1;
	}
	// self particle time
	void Run(){ tick++; }
	void doImpact(Carrier *f) {
		if (f != NULL) {
			if (headOfJump != NULL) {
				Jump *j; j = new Jump(FORWARD);  // Attention! Only forward
				j->next = headOfJump;
				headOfJump = j;
			} else {headOfJump = new Jump(FORWARD);};
		};
	}

};   // Leaf
//---------------------------------------------------------------------------

// pulse is time tick
// Is where Temp in composite?  Is't where Temp in particle?
class Temp {
public:
	int t; // number of time, it is istrument
	Temp *marked; // time mark
	Temp *next;
	bool lb; // it is base signal if true

	Temp() {next = NULL; marked = NULL; t = -1;}
	Temp(int tn) {  // with number of time
		next = NULL; t = tn;
		lb = false;
	}
};

	/******************************************************
	 *  Class:   <<Space>> ListItem
	 *  The class is container
	 *  ***
	 *  Concept = Cell of space
	 * ***************************************************/
class ListItem {
private:
	//Temp *curTemp;
protected:
public:
	Component *contents;
	ListItem *left, *right;
	Temp *tmp, *temp;
	int countTmp;  // debug
	int x;  // number of cell, it is instrument  - epistemology entity
	DataRecorder *observer;   //  - epistemology entity
	ListItem() {
	}
	ListItem(int xx, DataRecorder *o) {
		contents = NULL;
		left = NULL; right = NULL;
		x = xx; observer = o;  // instrument in cell - epistemology entity
		countTmp = 0;
	}

	// append item of local time
	void appTemp(Temp *tm) {
		countTmp++;   // debug: control value
		if (temp == NULL) {
			temp = new Temp(countTmp - 1); // t is countTmp-1
			tmp = temp;
		} else {
			tmp->next = new Temp(countTmp - 1);
			tmp = tmp->next;
		};
		tmp->marked = tm;   // synchronisation with global time
	}

	void resetTmp() {
		tmp = temp;
	}

	// <<Exist>>
	void ItemRun(Temp *tt, int tGlob, Carrier *c) {
		if (tmp != NULL) {
			if (tt == tmp->marked) {
				if (contents != NULL) {
					contents->Run();   // exist of particle
					observer->fixIt(tGlob, tt->t, x, tt->t, contents->tick);  // observe particle
					//print "ListItem is act:","for tt=marked=", tt.t, "ListItem=", self.x, "tloc=", self.tmp.t
					contents->doImpact(c); // interaction
					//observer.detect(tGlob,c); // observe act of interaction
				};
			tmp = tmp->next; // time run in cell
			};
		};
    }
};  //  ListItem

	/******************************************************
	 *  Class:   <<Ontology Category>> Composite
	 *  The class is Composite role in Composite pattern
	 *  ***
	 *  Concept = Physical space
	 * ***************************************************/
class Composite : public Component {
private:
protected:
	// particle motion
	void move() {
		ListItem *ll;
		// reset all particles
		ll = lst;
		while (ll != NULL) {
			if (ll->contents != NULL) ll->contents->reset();
		ll = ll->right;
		};
		// motion of particle
		ll = lst;
		while (ll != NULL) {
			if (ll->contents != NULL) {
				if (ll->contents->isActivity) {
					// place control
					//print "Particle in ",ll.x
					ll->contents->jumpp();
					ll->right->contents = ll->contents;
					ll->contents = NULL;
				};
			};
		ll = ll->right;
		};
	}  //  move()

	virtual Carrier *interaction(Carrier *c) = 0;
	//virtual Carrier *interaction(Carrier *c) {
	//	return NULL;
	//}

public:
	Temp *tmp;       // Global time
	ListItem *lst; // space
	Carrier *carr;   // interaction carrier

	//int tick;     // counter time - epistemology entity


	Composite() {
	}
	Composite(int sizeTick, int countTick, DataRecorder *ob) {

	carr = new Carrier(FORWARD);
	// Space and Time
	lst = new ListItem(0, ob);
	ListItem *ll; ll = lst;
	tmp = new Temp(0);
	Temp *tt; tt = tmp;
	int ii = 1;
	for (int k = 0; k < countTick; k++) {
		tt->lb = true;
		for (int i = 0; i < sizeTick; i++) {
			ll->right = new ListItem(ii, ob);
			tt->next = new Temp(ii);
			ll = ll->right;
			tt = tt->next;
			ii = ii + 1;
		};
	};
	int size = ii-1;    // debug: control value
	//print "Time count =", size
	// Synchronisation global and local time of spacetime

	int s; Temp *st;
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
						// control of marking
						// print "s=",s,"ListItem=",ll.x, "mark=", st.t  #marking debug
				};
			ll = ll->right;
			};
		};
	tt = tt->next;
	};
	// stend up to begin
	ll = lst;
	while (ll != NULL) {
		ll->resetTmp();
	ll = ll->right;
	};

} //   Composite(int sizeTick, int countTick, Observer *ob)

	// <<Exist>> operation
	void Run() {
		//t=0 is singular point
		tick = 0;
		Temp *tt; tt = tmp;
		ListItem *ll; ll = lst;
		Carrier *car; carr = interaction(carr);
		ll->ItemRun(tt, tick, car);

		tt = tt->next;
		// run of local time
		while (tt != NULL) {

			if (tt->lb) {
				tick = tick + 1;
				//print "World time =", self.tick
				move();
				//car = Carrier()
				car = interaction(carr);
			};
                
			ll = lst;
			while (ll != NULL) {
				ll->ItemRun(tt,tick, car);
				ll = ll->right;
			};

		tt = tt->next;
		};
	} // Run()


};

//---------------------------------------------------------------------------
#endif
```
