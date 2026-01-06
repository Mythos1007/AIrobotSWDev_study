//5개의 string문자열을 담을 수 있는 vector 또는 list를 선언하고 getline()함수를 이용하여 문자열을 입력받아 사전 순으로 가장 뒤에 나오는 문자열을 출력 문자열 비교는 <, > 연산자를 이용
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    vector<string> str;
    string input;

    for (int i = 0; i < 5; i++) {
        cout << "이름 >> ";
        getline(cin, input);
        str.push_back(input);
    }

    sort(str.begin(), str.end());

    cout << "사전 순으로 가장 뒤에 나오는 문자열: " << str.back() << endl;
    
    return 0;
}