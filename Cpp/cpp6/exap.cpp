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
        cout << "Drawing Circle" << endl;
    }
};

class Rect : public Shape {
public:
    virtual void draw() {
        cout << "Drawing Rectangle" << endl;
    }
};

class Line : public Shape {
public:
    virtual void draw() {
        cout << "Drawing Line" << endl;
    }
};

void paint(Shape* p) {
    p->draw();

    delete p;
}

int main() {
    paint(new Circle());
    paint(new Rect());
    paint(new Line());

    return 0;
}