#include <iostream>
#include <cstdlib>
#include <memory>
using namespace std;

class base {
    int a;
protected:
    void setA(int a) {
        this->a = a;
    }
public:
    void showA() {
        cout << a << endl;
    }
};

class Derived : public base {
    int b;
protected:
    void setB(int b) {
        this->b = b;
    }
public:
    void showB() {
        cout << b << endl;
    }
};

int main()
{
    
    return 0;
}