/*-----------------------------------------------------------------------*
 * name - class Component
 *
 *  Abstract class for Composite pattern
 *
 *-----------------------------------------------------------------------*/

class Component { // Concept = Subject of communication
private:
public:
AnsiString name;
AnsiString probe; //* <<Tool>> {Concept = Probe}
Component *next;
	void virtual Run() = 0;
// if this operation put to Component, then Component is Subject of communication
	AnsiString virtual getMessage() { //# {Concept = Send message} #//
	AnsiString rr = "?";
	return rr;
}
	void virtual putMessage(AnsiString s) { //$ {Concept = Resept message} $//
	}
};

/*-----------------------------------------------------------------------*
 * name - class Leaf
 *
 *  Leaf class for Composite pattern
 *
 *-----------------------------------------------------------------------*/

class Leaf : public Component { // Concept = Human
	class DialogList {
	public:
		AnsiString value;
		DialogList *next;
		DialogList(){
		value = ""; next = NULL;
		}
	};
private:
	DialogList *memory, *cm;
	AnsiString msg;
public:
	Leaf(AnsiString s) {
	name = s;
	memory = new DialogList;
	cm = memory;
	cm->value = "Good morning. How are you?.";
	cm->next = new DialogList;
	cm->next->value = "Not bad, thank you";
	cm = memory;
}
	void virtual Run() {// <<Exist>>
	if (msg.Length() != 0) cm = cm->next;
}
	AnsiString virtual getMessage() { //# {Concept = Send message} #//
	AnsiString rr;
	if (cm != NULL) rr = cm->value; else rr = "<end dialog>";
	return rr;
	}
	void virtual putMessage(AnsiString s) { //$ {Concept = Resept message} $//
	this->msg = s;
	}

};

/*-----------------------------------------------------------------------*
 * name - class Composite
 *
 *  Composite class for Composite pattern
 *
 *-----------------------------------------------------------------------*/

class Composite : public Component {
private:
protected:
	Component *pl;
public:
	Composit() {
	}
};

/*-----------------------------------------------------------------------*
 * name - class Node
 *
 *  Concrete class for Composite pattern
 *
 *-----------------------------------------------------------------------*/
class Node : public Composite {
private:
	AnsiString msg;
	void nextItem(){
	pl = pl->next;
	}
public:
	Node() {
	pl = new Leaf("Goldsmith");
	pl->next = new Leaf("Brown");
	msg="";
	}
//
void Run() { // <<Exist>>
	if (pl != NULL) {
	pl->putMessage(msg); pl->Run(); msg = pl->getMessage();
	this->nextItem();
	probe = msg; // measurement
	} else probe = "<close dialog>";
}
};
/*-----------------------------------------------------------------------*
 * name - class Root
 *
 *  Concrete class for Composite pattern
 *  Define initial and boundary conditions for Node class
 *
 *-----------------------------------------------------------------------*/

class Root : public Composite {
private:
public:
	Root() {
	this->pl = new Node;
	}
	void Run() { // <<Exist>>
	this->pl->Run();
	this->probe = this->pl->probe;
	}
};
