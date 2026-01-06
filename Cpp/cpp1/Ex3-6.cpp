#include <iostream>

using namespace std;
//메인 함수가 잘 작동 하도록 Rectangle 클래스를 완성하세요.
//두 멤버 변수와 3개의 생성자 그리고 isSquare() 함수를 가짐
class Rectangle {
public:
    int width;
    int height;
    
    Rectangle() {
        width = 1;
        height = 1;
    }

    Rectangle(int _w, int _h) {
        width = _w;
        height = _h;
    }

    Rectangle(int lenth) {
        width = lenth;
        height = lenth;
    }
    
    bool isSquare() {
        return width == height;
    }
};



int main(){
    Rectangle rect1; 
    Rectangle rect2(3, 5);
    Rectangle rect3(3); 

    if(rect1.isSquare()) cout << "rect1은 정사각형이다." << endl;
    if(rect2.isSquare()) cout << "rect2은 정사각형이다." << endl;
    if(rect3.isSquare()) cout << "rect3은 정사각형이다." << endl;

    return 0;
}
//출력
//rect1은 정사각형이다.
//rect3은 정사각형이다.