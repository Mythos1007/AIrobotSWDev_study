#include <stdio.h>

int per(int a)
{
    int sum;
    for (int i = 1; i < a; i++)
    {
        if (a % i == 0)
        {
            sum += i;
        }
    }
    if (sum == a)
    {
        printf("yes\n");
    }
    else
        printf("no\n");
}

int main()
{
    int a, b;
    scanf("%d", &a);
    per(a);
    scanf("%d", &b);
    per(b);
    return 0;
}