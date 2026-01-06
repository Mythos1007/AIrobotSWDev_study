#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <memory>
#include <vector>
#include <random>
using namespace std;

class Lotto
{
public:
    void generate()
    {
        random_device rd;
        mt19937 gen(rd());

        vector<int> pool(45);
        iota(pool.begin(), pool.end(), 1);

        shuffle(pool.begin(), pool.end(), gen);

        vector<int> lotto(pool.begin(), pool.begin() + 6);
        int bonus = pool[6];

        sort(lotto.begin(), lotto.end());

        cout << "로또 번호: ";
        for (int x : lotto)
        {
            cout << x << ' ';
        }
        cout << "\n보너스 번호: " << bonus << endl;
    }
};

int main()
{

    Lotto lotto;
    lotto.generate();
    return 0;
}