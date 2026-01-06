#include <iostream>

using namespace std;

class Calculator
{
public:
    Calculator() {}

    int plus(int x, int y)
    {

        return x + y;
    }

    int minus(int x, int y)
    {

        return x - y;
    }

    double divide(int x, int y)
    {

        return (double)x / y;
    }

    double multiple(int x, int y)
    {

        return x * y;
    }
};

int main()
{
    Calculator calc;
    cout << calc.plus(3, 5) << endl;
    cout << calc.minus(10, 4) << endl;
    cout << calc.divide(20, 4) << endl;
    cout << calc.multiple(6, 7) << endl;
    return 0;
}