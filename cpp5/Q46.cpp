#include <iostream>
#include <cstdlib>
#include <memory>
#include <vector>
using namespace std;

class Account
{
private:
    int id;
    string name;
    int balance = 0;
public:
    Account(int id, string name, int balance)
    {
        this->id = id;
        this->name = name;
        this->balance = balance;
    }
    int getId() const { return id; }
    string getName() const { return name; }
    int getBalance() const { return balance; }
    void deposit(int amount) {
        if (amount > 0) {
            balance += amount;
            cout << amount << "원이 입금되었습니다." << endl;
        }
    }
    bool withdraw(int amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            cout << amount << "원이 출금되었습니다." << endl;
            return true;
        }
        else {
            cout << "잔액이 부족합니다." << endl;
            return false;
        }
    }
    void printInfo() const {
        cout << "Account ID: " << id << ", 이름: " << name << ", 잔액: " << balance << endl;
    }
}; 
int main()
{
    Account acc1(1001, "홍길동", 50000);
    Account acc2(1002, "이순신", 30000);

    acc1.deposit(20000);
    acc2.withdraw(5000);
    acc2.withdraw(50000);

    acc1.printInfo();
    acc2.printInfo();

    vector<Account> v;
    v.push_back(acc1);
    v.push_back(acc2);

    cout << endl << "=== 전체 계좌 목록 ===" << endl;
    for (const auto& account : v) {
        account.printInfo();
    }
    
    return 0;
}