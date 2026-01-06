#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    FILE *fp;
    int ch;
//명령어 인자가 1개만 실행되지 않게 막아야한다 ?
    if(argc < 2) {
        printf("다음과 같이 사용하세요 : %s <파일명 또는 경로>\n", argv[0]);
        exit(2); //프로그램 자체를 종료
    }
    fp = fopen(argv[1], "r");
    if (fp == NULL)
    {
        printf("파일이 열리지 않았습니다.\n");
        return 1;
    }
    while (1)
    {
        ch = fgetc(fp);
        if (ch == EOF) //-1) 파일의 끝을 의미
        {
            break;
        }
        putchar(ch);
    }
    fclose(fp);

    return 0;
}