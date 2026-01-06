#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class UserInfo
{
private:
    string userName;
    string userEmail;

public:
    UserInfo(const string &userName,
             const string &userEmail)
        : userName(userName),
          userEmail(userEmail)
    {
    }

    const string &getName() const { return userName; }
    const string &getEmail() const { return userEmail; }

    void printUserInfo() const
    {
        cout << "[User] 이름: " << userName
             << ", 이메일: " << userEmail << endl;
    }
};

class ServerInfo
{
private:
    string serverIp;
    int serverPort;

public:
    ServerInfo(const string &ip, int port)
        : serverIp(ip), serverPort(port)
    {
    }

    const string &getIp() const { return serverIp; }
    int getPort() const { return serverPort; }

    void printServerInfo() const
    {
        cout << "[Server] IP: " << serverIp
             << ", Port: " << serverPort << endl;
    }
};

int main()
{

    UserInfo user("홍길동", "hong@example.com");
    ServerInfo server("192.168.0.10", 8080);

    user.printUserInfo();
    server.printServerInfo();

    return 0;
}