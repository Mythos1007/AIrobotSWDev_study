#include <iostream>
using namespace std;

class Base {
    public:
    virtual void f() { cout << "Base::f() called" << endl; }
};

class Derived : public Base {
    public:
    virtual void f() { cout << "Derived::f() called" << endl; 
    }
};

int main() {
    Derived d, *pDer;
    pDer = &d;
    pDer->f();  // Calls Derived::f()

    Base *pBase;
    pBase = pDer;  // Upcasting Derived* to Base*
    pBase->f();    // Calls Derived::f() because f() is virtual
    return 0;
    }