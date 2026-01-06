#include <iostream>
using namespace std;

class Shape {
public:
    void draw() {
        cout << "도형을 그리다" << endl;
    }
};
class Triangle : public Shape {
public:
    void draw() override {
        cout << "삼각형을 그리다" << endl;
    }
};
class Rectangle : public Shape {
public:
    void draw() override {
        cout << "사각형을 그리다" << endl;
    }
};
class Circle : public Shape {
public:
    void draw() override {
        cout << "원을 그리다" << endl;
    }
};
int main()
{
    Shape* s1 = new Shape();
    s1->draw();
    Shape* s2 = new Triangle();
    s2->draw();
    Shape* s3 = new Rectangle();
    s3->draw();
    Shape* s4 = new Circle();
    s4->draw();

//부모 클래스의 포인터로 자식 클래스의 객체를 가리키는 다형성
    delete s1;
    delete s2;
    delete s3;
    delete s4   ;

    return 0;


}