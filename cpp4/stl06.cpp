#include <iostream>
#include <cstdlib>
#include <memory>
#include <map>
using namespace std;

int main()
{
    map<string, string> dic;

    dic.insert(make_pair("love", "사랑"));
    //dic["love"] = "사랑";
    
    string kor = dic["love"];
    string kor2 = dic.at("love");

    cout << kor << endl;
    cout << kor2 << endl;

    return 0;
}