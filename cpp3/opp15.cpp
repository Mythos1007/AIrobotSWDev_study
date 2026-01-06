#include <iostream>
#include <cstdlib>
#include <memory>
using namespace std;

class Weapon {
protected:
    int level;
    string name;
public:
    Weapon() {
        level = 1;
        name = "무기";
    }
    virtual void attack() {
        cout << name << "로 공격!" << endl;
    }
    virtual ~Weapon() {}
    void showLevel() {
        cout << name << "level : " << level << endl;
    }

    void showName() {
        cout << "name : " << name << endl;
    }
};

class Sword : public Weapon {
public:
    Sword() {
        level = 1;
        name = "검 ";
    }

    void attack() override {
        cout << name << "으로 공격!" << endl;
    }
};

class Axe : public Weapon {
public:
    Axe() {
        level = 1;
        name = "도끼 ";
    }
    void attack() override {
        cout << name << "으로 공격!" << endl;
    }
};
int main()
{
    Weapon* weapon = new Weapon();
    weapon->attack();
    weapon->showLevel();
    weapon->showName();

    delete weapon;

    unique_ptr<Sword> sword = make_unique<Sword>();
    sword->attack();
    sword->showLevel();
    sword->showName();

    return 0;
}