//다음 벡터에서 STL함수를 사용하여 중복을 제거한 후 출력하라.
//hint : sort, unique, erase
#include <iostream>
#include <cstdlib>
#include <memory>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<int> vec = {1, 1, 1, 2, 2, 2, 3, 3, 3};

    sort(vec.begin(), vec.end());
    vec.erase(unique(vec.begin(), vec.end()), vec.end());
    for (int i : vec)
        cout << i << " ";
}