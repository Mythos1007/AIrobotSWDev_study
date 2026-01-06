#include <iostream>
using namespace std;

class Cat {
private:
    string name;
    int age;
    string color;
public:
    //디폴트 생성자
    Cat() {
        name = "Tom";
        age = 3;
        color = "navy";
    }
    //인자가 있는 생성자
    Cat(string _name, int _age, string _color) {
        name = _name;
        age = _age;
        color = _color;
    }

    //Getter & Setter
    string getName() {
        return name;
    }

    void setName(string _name) {
        name = _name;
    }

    int getAge() {
        return age;
    }

    void setAge(int _age) {
        age = _age;
    }

    string getColor() {
        return color;
    }
    
    void setColor(string _color) {
        color = _color;
    }
    
};

int main() {
    Cat tom;
    
    cout << "이름 : " << tom.getName() << ", 나이 : " << tom.getAge() << ", 색깔 : " << tom.getColor() << endl;

    Cat* cheeze = new Cat("Cheeze", 2, "yellow");
    cout << "이름 : " << cheeze->getName() << ", 나이 : " << cheeze->getAge() << ", 색깔 : " << cheeze->getColor() << endl;
    delete cheeze;
    return 0;

}
