#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct cracker
{
    int carc;
    int price;
};

int main()
{
    struct cracker crack;
    scanf("%d %d", &crack.price, &crack.carc);

    printf("가격 : %d원\n", crack.price);
    printf("열량 : %d칼로리\n", crack.carc);
}