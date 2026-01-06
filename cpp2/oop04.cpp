#include <iostream>
using namespace std;

class Shape {
public:
    virtual void draw() {
        cout << "도형을 그린다 ~~~" << endl;
    }
    virtual ~Shape() {}
}; 
//부모 클래스 virtual 소멸자 추가
class Triangle : public Shape {
public:
    void draw() override{
        cout << "삼각형을 그린다 ~~~" << endl;
    }
};  
class Rectangle : public Shape {
public:
    void draw() override{
        cout << "사각형을 그린다 ~~~" << endl;
    }
};
class Circle : public Shape {
public:
    void draw() override{
        cout << "원형을 그린다 ~~~" << endl;
    }
};
int main() {

    Shape* shape[4];
    shape[0] = new Shape();
    shape[1] = new Triangle();
    shape[2] = new Rectangle();
    shape[3] = new Circle();

    for(auto s : shape) {
        s->draw();
    }
    // for (int i = 0; i < 4; i++) {
    //     shape[i]->draw();
    // }
    for (int i = 0; i < 4; i++) {
        delete shape[i];
    }

    return 0;
    
}