#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
using namespace std;

class Lotto
{
private:
    vector<int> lotto;
    int bonus;

public:
    Lotto()
    {
        random_device rd;
        mt19937 gen(rd());

        vector<int> num(45);
        iota(num.begin(), num.end(), 1);

        shuffle(num.begin(), num.end(), gen);

        vector<int> lotto(num.begin(), num.begin() + 6);
        int bonus = num[6];

        sort(lotto.begin(), lotto.end());
    }
};

int main()
{
    Lotto l;
    l.print();

    return 0;
}