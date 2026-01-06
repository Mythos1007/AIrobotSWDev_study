#include <iostream>

using namespace std;

class Circle {
public:
    void getArea() {
        const double pi = 3.14;
        double radius = 5.0;
        double area = pi * radius * radius;
        cout << "원의 넓이: " << area << endl;
    }

};

int main() {

    Circle circle;
    Circle& ref = circle;

    ref.getArea();
    return 0;
}