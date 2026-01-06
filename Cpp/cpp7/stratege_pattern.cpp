#include <iostream>
#include <memory>
using namespace std;

//anstract strategy
class IAttackStrategy {
public:
    virtual void attack() = 0; //가장 핵심 함수 ? 추상 함수 ?

    virtual ~IAttackStrategy() = default;
};

//starategy class 화공 수공 물리
class FireAttack : public IAttackStrategy {
public:
    void attack() override {
        cout << "Fire Attack!" << endl;
    }
};
class WaterAttack : public IAttackStrategy {
public:
    void attack() override {
        cout << "Water Attack!" << endl;
    }
};
class PhysicalAttack : public IAttackStrategy {
public:
    void attack() override {
        cout << "Physical Attack!" << endl;
    }
};
//context class 
class Character {
private:
    string name;
    IAttackStrategy* strategy; //포인터로 전략을 가리킴?
public:
    Character(string name): name(name){}
    void setStrategy(IAttackStrategy& strategy) {
        this->strategy = &strategy;
    }
    void attack() {
        strategy->attack();
    }
};

int main() {
    Character hero("이순신");
    FireAttack fire;
    
    hero.setStrategy(fire);
    hero.attack();
}