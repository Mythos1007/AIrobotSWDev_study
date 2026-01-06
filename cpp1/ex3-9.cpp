#include <iostream>
using namespace std;

class Person {

private:
    int stNumber;
    string name;

public:
    Person() {}
    Person(int _stNumber, string _name) {
        stNumber = _stNumber;
        name = _name;
    }
    void setStNumber(int _stNumber) {
        stNumber = _stNumber;
    }
    int getStNumber() {
        return stNumber;
    }
    void setName(string _name) {
        name = _name;
    }
    string getName() {
        return name;
    }

};

int main()
{
    Person sma(1, "샘");
    cout << "시민번호 : " << sma.getStNumber() << endl;
    cout << "이름 : " << sma.getName() << endl;

    Person jane;
    jane.seyname("제인");
    jane.setStNumber(2);
    cout << "시민번호 : " << jane.getStNumber() << endl;
    cout << "이름 : " << jane.getName() << endl;
    
    return 0;
}