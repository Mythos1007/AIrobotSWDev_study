#include <iostream>

using namespace std;

class lion {
public:
    void body() {
        cout << "튼튼한 사자의 몸통" << endl;
    }
    
};

class eagle {
public:
    void body() {
        cout << "날렵한 독수리의 머리와 날개" << endl;
    }
};

class griffin : public lion, public eagle {};

int main() {
    griffin g;
    g.lion::body();   
    g.eagle::body();  
    return 0;
}