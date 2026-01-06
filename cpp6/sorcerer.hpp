#pragma once

#include <iostream>
#include <string>
using namespace std;

class Sorcerer
{
private:
    string name;
    string leftWeapon;
    string rightWeapon;
    string leftRing;
    string rightRing;
    string armor;
    string amulet;

    Sorcerer(const string &name,
             const string &leftWeapon,
             const string &rightWeapon,
             const string &leftRing,
             const string &rightRing,
             const string &armor,
             const string &amulet)
        : name(name),
          leftWeapon(leftWeapon),
          rightWeapon(rightWeapon),
          leftRing(leftRing),
          rightRing(rightRing),
          armor(armor),
          amulet(amulet)
    {
    }

public:
    class Builder
    {
    private:
        string name;
        string leftWeapon = "맨손";
        string rightWeapon = "맨손";
        string leftRing = "없음";
        string rightRing = "없음";
        string armor = "천 갑옷";
        string amulet = "없음";

    public:
        Builder(const string &name) : name(name) {}
        Builder &setLeftWeapon(const string &weapon)
        {
            leftWeapon = weapon;
            return *this;
        }
        Builder &setRightWeapon(const string &weapon)
        {
            rightWeapon = weapon;
            return *this;
        }
        Builder &setLeftRing(const string &ring)
        {
            leftRing = ring;
            return *this;
        }
        Builder &setRightRing(const string &ring)
        {
            rightRing = ring;
            return *this;
        }
        Builder &setArmor(const string &armorName)
        {
            armor = armorName;
            return *this;
        }
        Builder &setAmulet(const string &amuletName)
        {
            amulet = amuletName;
            return *this;
        }
        Sorcerer build()
        {
            return Sorcerer(
                name,
                leftWeapon,
                rightWeapon,
                leftRing,
                rightRing,
                armor,
                amulet);
        }
    };

    void print() const
    {
        cout << "===== 원소술사 장비 =====" << endl;
        cout << "이름        : " << name << "\n";
        cout << "왼손 무기   : " << leftWeapon << "\n";
        cout << "오른손 무기 : " << rightWeapon << "\n";
        cout << "왼손 반지   : " << leftRing << "\n";
        cout << "오른손 반지 : " << rightRing << "\n";
        cout << "갑옷        : " << armor << "\n";
        cout << "목걸이      : " << amulet << "\n";
        cout << "===========================\n";
    }
};
