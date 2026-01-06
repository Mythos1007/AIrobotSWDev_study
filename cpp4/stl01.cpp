#include <iostream>
#include <cstdlib>
#include <memory>
using namespace std;

template <class T>
void mySwap(T& a, T& b)
{
    T temp = a;
    a = b;
    b = temp;
}
int main()
{
    int a = 10, b = 20;
    mySwap(a, b);
    cout << "a: " << a << ", b: " << b << endl;
       
    return 0;
}