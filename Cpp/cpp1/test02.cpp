#include <iostream>
using namespace std;    

class Knight {
public:
    int level;
    string name;
    int hp;
    int mp;

    Knight(){
        level = 1;
        name = "기사";
        hp = 100;
        mp = 50;
    }

    Knight(string _name, int _level){
        name = _name;
        level = _level;
        hp = 100;
        mp = 50;
    }

    Knight(string _name, int _level, int _hp, int _mp){
        name = _name;
        level = _level;
        hp = _hp;
        mp = _mp;
    }
    string attack(){
    return name + "이(가) 공격합니다!";
    }
    string attack(string weapon){
        return name + "이(가) " + weapon + "(으)로 공격합니다!";
    }
    string defend(){
        return name + "이(가) 방어합니다!";
    }
    string eat(){
        return name + "이(가) 음식을 먹습니다!";
    }
};

int main()   
{
    Knight aryng("설아량", 12, 1, 1);
    cout << "나이 : " << aryng.level << endl;
    cout << "이름 : " << aryng.name << endl;
    cout << "체력 : " << aryng.hp << endl;
    cout << "마나 : " << aryng.mp << endl;
    cout << aryng.attack() << endl;
    cout << aryng.attack("나비") << endl;
    cout << aryng.defend() << endl;
    cout << aryng.eat() << endl;
    return 0;

}