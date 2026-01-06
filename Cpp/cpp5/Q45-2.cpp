//게임을 만드는 중 게임에는 다음과 같은 캐릭터가 존재
//Knight(검으로 공격), Archer(활로 공격), Wizard(마법으로 공격)
//질문
//이 세 캐릭터가 동격하는 행위를 공통화하려면 어던 상속구조를 만들 수 있을까 ?
//최상위 부모클래스 Hero
//객체를 만들 때 부모클래스 포인터로 자식클래스의 함수가 동작되도록 만들기
//응용개념 : 상속, 가상함수, 다형성 //단 객체의 생성은 unique_ptr로 작성
#include <iostream>
#include <cstdlib>
#include <memory>
#include <string>
#include <vector>
using namespace std;

class Hero
{
public:
    virtual void attack()
    {
        cout << "공격한다 ~~" << endl;
    }
};
class Knight : public Hero
{
public:
    void attack() override
    {
        cout << "검으로 공격한다 ~~" << endl;
    }
};
class Archer : public Hero
{
public:
    void attack() override
    {
        cout << "활로 공격한다 ~~" << endl;
    }
};
class Wizard : public Hero
{
public:
    void attack() override
    {
        cout << "마법으로 공격한다 ~~" << endl;
    }
};
int main()
{
    unique_ptr<Hero> knight = make_unique<Knight>();
    unique_ptr<Hero> archer = make_unique<Archer>();
    unique_ptr<Hero> wizard = make_unique<Wizard>();

    knight->attack();
    archer->attack();
    wizard->attack();

    
    return 0;
}