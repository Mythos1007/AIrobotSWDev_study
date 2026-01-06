#include <iostream>
#include <cstdlib>
using namespace std;

class Circle {
public:
    int radius;
    Circle() {}
    Circle(int r) { radius = r; }
    double getArea() {
        return 3.14 * radius * radius; 
    }
};
int main()
{
    Circle circleArray[3] = {Circle(10), Circle(20), Circle(1)};    
    for (int i = 0; i < 3; i++) {
        cout << i << "번째 원의 넓이: " << circleArray[i].getArea() << endl;
    }

    cout << "프로그램이 동작하였습니다" << endl;
    
    return 0;
}