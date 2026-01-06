#include <iostream>
using namespace std;

class Student {
private:
    string name;
    int age;
    string major; 
    int id;

    Student(const string& name, int age, const string& major, int id)
        : name(name), age(age), major(major), id(id) {}
public:
    class Builder {
    private:
        string name;
        int age = 0;
        string major = "Undeclared";
        int id = 0;
    public:
        Builder& setName(const string& name) {
            this->name = name;
            return *this;
        }
        Builder& setAge(int age) {
            this->age = age;
            return *this;
        }
        Builder& setMajor(const string& major) {
            this->major = major;
            return *this;
        }
        Builder& setId(int id) {
            this->id = id;
            return *this;
        }
        Student build() {
            return Student(name, age, major, id);
        }
    };
    string getname() const { return name; }
    int getage() const { return age; }
    string getmajor() const { return major; }
    int getid() const { return id; }
};

int main() {
    Student student = Student::Builder()
                        .setName("홍길동")
                        .setAge(20)
                        .setMajor("Embedded System")
                        .setId(20251234)
                        .build();

    cout << "Student Info" << endl;
    cout << "Name: " << student.getname() << endl;
    cout << "Age: " << student.getage() << endl;
    cout << "Major: " << student.getmajor() << endl;
    cout << "ID: " << student.getid() << endl;

    return 0;
}