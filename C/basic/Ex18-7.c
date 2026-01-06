#include <stdio.h>
#include <string.h>

int main()
{
    FILE *fp;
    char str[20];

    fp = fopen("a.txt", "a+"); //r+ - 읽고 쓰기위해 개방 w+지우고 쓰기위해 해방 a+ 읽거나 파일의 끝에 추가하기 위해 개방
    if (fp == NULL)
    {
        printf("파일을 만들지 못했습니다.\n");
        return 1;
    }

    while (1) //무한루프
    {
        printf("과일 이름 : ");
        scanf("%s", str);
        if (strcmp(str, "end") == 0)
        {
            break;      
        }
        else if (strcmp(str, "list") == 0)
        {
            fseek(fp, 0, SEEK_SET);// 모드에서 읽고 쓰기를 바꿀 때 필요함 SET-처음 CUR-현재위치 END-끝
            while (1)
            {
                fgets(str, sizeof(str),fp);
                if (feof(fp))//feof함수는 파일의 끝이면 참을 반환함 (0이아닌 값)
                {
                    break;
                }
                printf("%s", str);
            }
        }
        else 
        {
            fprintf(fp, "%s\n", str);
        }
    }
    fclose(fp);

    return 0;
}