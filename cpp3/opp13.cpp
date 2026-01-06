#include <iostream>
#include <cstdlib>
using namespace std;

class Person {};

class Student : public Person {};

int main()
{
    Person GilDong;
    unique_ptr<Person> chulsu = make_unique<Person>();

    
    
    return 0;
}