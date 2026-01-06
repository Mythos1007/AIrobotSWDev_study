#include <iostream>
using namespace std;

class Circle() {
private:
    double radius;
public:
    Circle() {
        this->radius = 1.0;
    }
    Circle(int r) {
        this->radius = r;
    }
}