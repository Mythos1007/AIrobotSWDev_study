#include <iostream>
using namespace std;

class horse {
public:
    void run() {
        cout << "달리다 ~!!" << endl;
    }
};  

class Bird {
public:
    void fly() {
        cout << "날다 ~!!" << endl;
    }
};

class Pegasus : public horse, public Bird {

};

int main() {
    Pegasus p;
    p.run(); // horse 클래스의 run() 메서드 호출
    p.fly(); // Bird 클래스의 fly() 메서드 호출
    return 0;
}