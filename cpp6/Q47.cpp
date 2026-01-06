#include <iostream>
#include <string>
#include "paladin.hpp"
#include "sorcerer.hpp"

using namespace std;

int main()
{
    Paladin paladin = Paladin::Builder("팔라딘")
                          .setLeftWeapon("성스러운 망치")
                          .setRightWeapon("성스러운 방패")
                          .setLeftRing("신념의 반지")
                          .setRightRing("믿음의 반지")
                          .setArmor("성스러운 갑옷")
                          .setAmulet("신성한 목걸이")
                          .build();

    paladin.print();

    Sorcerer pyro = Sorcerer::Builder("파이로")
                        .setLeftWeapon("루비 지팡이")
                        .setRightWeapon("화염의 수정구슬")
                        .setLeftRing("불의 영혼 반지")
                        .setRightRing("이그니스의 숨결")
                        .setArmor("태양불꽃 갑옷")
                        .setAmulet("태양석 목걸이")
                        .build();
    pyro.print();

    Sorcerer noob = Sorcerer::Builder("초보자")
                        .setRightWeapon("보급형 지팡이")
                        .setArmor("낡은 천 로브")
                        .build();
    noob.print();
    return 0;
}