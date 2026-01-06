#include <iostream>
using namespace std;  

void fillline(int n=25, char c='*') {
    for(int i = 0; i < n; i++)
        cout << c;
    cout << endl;
}

int main() {
    fillline();
    fillline(10, '%');
}