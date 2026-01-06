#include <iostream>
using namespace std;

class Shape {
public:
    virtual void draw() {
        cout << "Drawing Shape" << endl;
    }
};

class Circle : public Shape {
public:
    virtual void draw() {
        Shape::draw();
        cout << "Drawing Circle" << endl;
    }
};

int main() {
    Circle circle;
    Shape * pShape = &circle;

    pShape->draw();
    pShape->Shape::draw();

    return 0;
}