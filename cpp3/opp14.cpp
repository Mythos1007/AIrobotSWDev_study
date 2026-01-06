#include <iostream>
#include <cstdlib>
#include <memory>
using namespace std;

class Hero {
private:
    string tresure;
protected:
    int level;
    string name;
public:
    int mp; 

    Hero() {
        tresure = "보물";
        level = 1;
        name = "영웅";
        mp = 10;
    }
};
class Wizard : public Hero {
public:
    Wizard() {
        level = 5;
        name = "마법사";
        mp = 100;
    }
};

int main()
{
    //unique_ptr<Wizard> geralt - make_unique<Wizard>();
    Wizard geralt;
    cout << geralt.mp << endl;

    return 0;
}