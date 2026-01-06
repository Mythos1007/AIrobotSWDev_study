#include <iostream>
#include <cstdlib>
#include <memory>
#include <string>
using namespace std;

class Calculater
{
private:
    double num1;
    double num2;
public:
    void input()
    {
        cout << "입력" << endl;
        cin >> num1;
        cin >> num2;
        this->num1 = num1;
        this->num2 = num2;
    }
    void add()
    {
        return num1 + num2;
    }
    void minus()
    {
        return num1 - num2;
    }
    void multiply()
    {
        return num1 * num2;
    }
    void divide()
    {
        if (num2 == 0)

        {
            cout << "0으로 나눌 수 없습니다." << endl;
            return;
        };
    }
};
int main()
{
    
    unique_ptr<Calculater> calcPtr = make_unique<Calculater>();
    
    calcPtr->input();
    cout << "덧셈: " << calcPtr->add() << endl;
    cout << "뺄셈: " << calcPtr->minus() << endl;
    cout << "곱셈: " << calcPtr->multiply() << endl;
    cout << "나눗셈: " << calcPtr->divide() << endl;
    return 0;
}