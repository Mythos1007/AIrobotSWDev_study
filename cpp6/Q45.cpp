#include <iostream>
#include <memory>
#include <vector>
using namespace std;

class Hero {
public:
    virtual void attack() { cout << "공격한다 ~~" << endl; }
    virtual ~Hero() = default;

};

class Knight : public Hero {
public:
    void attack() override { cout << "검으로 공격한다 ~~" << endl; }
};

class Archer : public Hero {
public:
    void attack() override { cout << "활로 공격한다 ~~" << endl; }
};

class Wizard : public Hero {
public:
    void attack() override { cout << "마법으로 공격한다 ~~" << endl; }
};

int main() {

    vector<Hero*> hero_list;
    unique_ptr<Knight> k = make_unique<Knight>();
    unique_ptr<Archer> a = make_unique<Archer>();
    unique_ptr<Wizard> w = make_unique<Wizard>();

    hero_list.push_back(k.get());
    hero_list.push_back(a.get());
    hero_list.push_back(w.get());
    for (auto h : hero_list) {
        h->attack();
    }

    return 0;
}