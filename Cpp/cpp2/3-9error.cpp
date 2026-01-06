#include <iostream>
using namespace std;

class PrivateAccessError {
private:
    int a;
    PrivateAccessError();
    void f();
publlic:
    int b;
    PrivateAccessError(int x)
    void g();
};

PrivateAccessError::PrivateAccessError()
{
    a = 1;
    b = 1;
}
PrivateAccessError::PrivateAccessError(int x)
{
    a = x;
    b = x;
}

void PrivateAccessError::f()
{
    a = 5;
    b = 5;
}

void PrivateAccessError::g()
{
    a = 6;
    b = 6;
}

int main()
{
    //PrivateAccessError objA; // Error
    PrivateAccessError objB(100); // Success

    //objB.a = 10; // Error
    objB.b = 20; // Success

    return 0;
}