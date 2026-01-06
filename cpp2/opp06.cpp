#include <iostream>
#include <cstdlib>
using namespace std;

class Circle {
    int radius;
public:
    Circle() { radius = 1; }   
    Circle(int r) { radius = r; }
    void setRadious(int r) { radius = r; }
    double getArea();
};
double Circle::getArea() {
    return 3.14 * radius * radius;
}
    int main()
{
    Circle cir[3];
    cir[0].setRadious(10);
    cout << "area : " << cir[0].getArea() << endl;
    Circle* p;
    p = cir;
    cout << "area : " << p[0].getArea() << endl;

    Circlr* cir2[3];
    cir2[0] = new Circle();
    cir2[0]->setRadious(10);
    cout << "area : " << cir2[0]->getArea() << endl;

    delete cir2[0];
    return 0;

}