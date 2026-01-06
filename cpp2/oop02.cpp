#include <iostream>
using namespace std;


class Car {
public:
    int speed;
    string brand;

    Car() {
        speed = 0;
        brand = "Generic";
    }
    void run() {
        cout << "차가 달린다 ~~~" << endl;
        cout << "브랜드 : " << brand  <<endl;
    }

};
class SuperCar : public Car {
public:
    int booster;
    SuperCar() {
        booster = 100;
    }
    void run() {
        cout << booster << "용량으로 " << " 차가 엄청나게 달린다 ~~~" << endl;
    }
};
int main() {
    Car car;
    car.run();
    SuperCar superCar;
    superCar.run();

    return 0;
}