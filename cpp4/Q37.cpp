#include <iostream>
#include <cstdlib>
#include <memory>
using namespace std;

template <typename T>
T add(T arr[], int size)
{
    T sum = 0;
    for (int i = 0; i < size; i++)
    {
        sum += arr[i];
    }
    return sum;
}
int main()
{
    int x[] = {1, 2, 3, 4, 5};
    double y[] = {1.2, 2.3, 3.4, 4.5, 5.6, 6.7};

    cout << "sum of x: " << add(x, 5) << endl;
    cout << "sum of y: " << add(y, 6) << endl;
    return 0;
}