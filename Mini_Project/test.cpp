#include <iostream>
#include <chrono>

int main()
{
    std::chrono::system_clock::time_point start =
        std::chrono::system_clock::now();
    int sum = 0;
    while (true)
    {
        int sum = 0;
        for (int i = 0; i < 1000000; ++i)
        {
            sum += i;
            std::chrono::duration<double> sec = std::chrono::system_clock::now() - start;
            if (int(sec.count()) % 1 == 0)
                std::cout << "현재 시간 : " << sec.count() << "초, 합계: " << sum << std::endl;
        }
    }
}