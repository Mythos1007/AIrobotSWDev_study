#include <iostream>
#include <string>
using namespace std;
class Car
{
public:
//1. 멤버변수 
    int speed;
    string brand;
    string color;

//2. 생성자 
    Car():speed(150), brand("Audi"), color("black"){

    }

//3. 멤버 메소드
    string run(){
        return "달린다 ~~!";
    }

};

int main()
{
    

    Car mycar;
    cout << "myCar.speed : " << mycar.speed << endl;
    cout << "myCar.brand : " << mycar.brand << endl;
    cout << "muCar.color : " << mycar.color << endl;
    cout << "run : " << mycar.run() << endl;
    return 0;
}