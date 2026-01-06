#include <iostream>
#include <memory>

class Person {};
class Professional : public Person {};

int main()
{
//스마트 포인터 기법을 사용해서 heap 메모리에 leesunsin을 생성

    Progessor* lee = new Professor();
    delete lee; //메모리 해제
    unique_ptr<Professional> leesunsin = make_unique<Professional>();



    return 0;
}