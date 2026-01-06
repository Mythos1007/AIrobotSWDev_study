#include <iostream>
#include <string>
using namespace std;

void msg(int id) {
    cout << id << endl;
}

void msg(int id, string str="") {
    cout << id << ": " << str << endl;
}

int main() {
    msg(5, "Hello");
    msg(10);
}
