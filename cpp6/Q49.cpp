#include <iostream>
using namespace std;

class Car {
private:
    string brand;
    int speed;
    string color;

    Car(const string& brand, int speed, const string& color)
        : brand(brand), speed(speed), color(color) {}
public:
    class Builder {
    private:
        string brand;
        int speed = 0;
        string color;
        
    public:
        Builder& setBrand(const string& b) {
            brand = b;
            return *this;               
        }
        Builder& setSpeed(int s) {
            speed = s;
            return *this;               
        }
        Builder& setColor(const string& c) {
            color = c;
            return *this;               
        }
        Car build() {
            return Car(brand, speed, color);
        }   
    };
  
    string getBrand() { return brand; }
    int getSpeed() { return speed; }
    string getColor() { return color; }
};

int main() {
    Car car = Car::Builder()
                    .setBrand("BMW")
                    .setSpeed(250)
                    .setColor("Black")
                    .build();

    cout << "자동차 정보" << endl;
    cout << "Brand: " << car.getBrand() << endl;
    cout << "Speed: " << car.getSpeed() << endl;
    cout << "Color: " << car.getColor() << endl;

    return 0;
}