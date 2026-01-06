#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct book
{
    char title[20];
    char author[40];
    int page;
    int price;

};

int main()
{
    struct book C = {"C프로그래밍", "데니스", 180, 18000};
    printf("책 제목 : %s\n", C.title);
    printf("저자 : %s\n", C.author);
    printf("페이지 수 : %d페이지\n", C.page);
    printf("가격 : %d원", C.price);
    
}