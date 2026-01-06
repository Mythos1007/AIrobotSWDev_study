//getline함수를 사용하여 문자열로 두 정수를 입력받아 stoi함수를 사용해 삼각형의 넓이를 구하는 프로그램 작성 //멤버 함수로 getArea()를 구현하여 사각형의 넓이를 구하는 프로그램 작성
#include <iostream>
#include <string>
using namespace std;
class Triangle {
private:
    int width;
    int height;
public:
    Triangle() {
        width = 1;
        height = 1;
    }
    Triangle(int w, int h) {
        this->width = w;
        this->height = h;
    }
    double getArea() {
        return (width * height) / 2.0;
    }
};
int main() {
    string width, height;
    cout << "삼각형의 밑변과 높이를 입력하세요 : ";
    getline(cin, width, ' ');
    getline(cin, height);

    Triangle tri(stoi(width), stoi(height));
    cout << "삼각형의 넓이 : " << tri.getArea() << endl;

    return 0;
   
}