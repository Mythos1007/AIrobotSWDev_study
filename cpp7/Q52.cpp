#include <iostream>
using namespace std;

class Magic
{
public:
    virtual void cast() = 0;
    virtual ~Magic() = default;
};
class FireMagic : public Magic
{
public:
    void cast() override
    {
        cout << "해리가 화염 마법으로 공격합니다!!!" << endl;
    }
};
class IceMagic : public Magic
{
public:
    void cast() override
    {
        cout << "해리가 얼음 마법으로 공격합니다!!!" << endl;
    }
};
class Harry
{
private:
    string name;
    Magic *current = nullptr;

public:
    Harry(string name) : name(name) {}

    void setMagic(Magic &magic)
    {
        current = &magic;
    }

    void Attack()
    {
        if (!current)
            cout << "[시스템] 마법이 설정되지 않았습니다." << endl;
        else
            return current->cast();
    }
};

int main()
{
    Harry harry("해리 포터");
    FireMagic fire;
    IceMagic ice;

    int choice;
    do
    {
        cout << "=== 해리 포터 마법 전투 시뮬레이터 ===" << endl;
        cout << "1. 화염 마법 선택" << endl;
        cout << "2. 얼음 마법 선택" << endl;
        cout << "3. 공격 실행" << endl;
        cout << "0. 종료" << endl;
        cout << "메뉴 선택 : ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            harry.setMagic(fire);
            cout << "[시스템] 해리가 화염 마법을 준비합니다." << endl;
            break;
        case 2:
            harry.setMagic(ice);
            cout << "[시스템] 해리가 얼음 마법을 준비합니다." << endl;
            break;
        case 3:
            harry.Attack();
            break;
        case 0:
            cout << "프로그램을 종료합니다." << endl;
            break;
        default:
            cout << "잘못된 선택입니다. 다시 시도하세요." << endl;
        }
        cout << "----------------------------------------" << endl;
    } while (choice != 0);

    return 0;
}