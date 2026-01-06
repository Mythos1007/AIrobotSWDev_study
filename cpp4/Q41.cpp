//1 ~ 20 까지 정수가 들어있는 벡터변수가 있다 람다 표현식을 사용해서 홀수만 출력

#include <iostream>
#include <cstdlib>
#include <memory>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<int> v ;
    for (int i = 1; i <= 20; i++)
        v.push_back(i);

    for_each(v.begin(), v.end(), [](int n) {
        if (n % 2 != 0)
            cout << n << " ";
        });
    cout << endl;
    return 0;
}