#include <iostream>
#include <cstdlib>
#include <memory>
using namespace std;

class TV {
    protected:
    int size;
    public:
    TV() {
        size = 20;
    }
    TV(int size) {
        this->size = size;
    }
    int getSize() {
        return this->size;
    }

};
class WideTV : public TV {
protected:
    bool videoIn;
public:
    WideTV(int size, bool videoIn) : TV(size) {
        this->videoIn = videoIn;
    }
    bool getVideoIn() {
        return this->videoIn;
    }
};
class SmartTV : public WideTV {
protected:
    string ipAddress;
public:
SmartTV(string ipAddr, int size): WideTV(size, true) {
        this->ipAddress = ipAddr;
    }
    string getIpAddress() {
        return this->ipAddress;
    }
};
int main()
{
    SmartTV htv("192.0.0.1", 32);
    cout << "size : " << htv.getSize() << endl;
    cout << "videoIn : " << htv.getVideoIn() << endl;
    cout << "IP : " << htv.getIpAddress() << endl;
    return 0;
}