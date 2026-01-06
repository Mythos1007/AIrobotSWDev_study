#include <stdio.h>

int prime()
{
    int pri = 1;
    for (int i = 2; i <= 100; i++)
    {
        int pri = 1;
        for (int k = 2; k < i; k++)
        {
            if (i % k == 0)
            {
                pri = 0;
                break;
            }
        }
        if (pri == 1)
        {
            printf("%d ", i);
        }
    }
    return 0;
}
int main()
{
    prime();
    return 0;
}