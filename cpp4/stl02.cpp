#include <iostream>
#include <cstdlib>
#include <memory>
using namespace std;
#include <vector>

int main()
{
    vector<int> vec;
    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(3);
    
    //cout << "size : " >> vec.size() << endl;
    for (int i = 0; i < vec.size(); i++) {
        cout << vec[i] << " ";
    }

    cout << endl;
    return 0;
}