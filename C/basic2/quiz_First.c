#include <stdio.h>

int main()
{
    FILE *fp;    
    FILE *fo;
    int ch;
    char str[80];
    int i = 0;
    fp = fopen("read.txt", "r");

    if (fp == NULL)
    {
        printf("파일을 읽어오지 못했습니다.\n");
        return 1;
    }
    while ((ch=fgetc(fp)) != EOF)
    {
        str[i] = (char)ch;
        i++;
    }
    str[i] = '\0';
    fclose(fp);

    fo = fopen("write.txt", "w");
    fprintf(fo, "%s\n", str);
    fclose(fo);

    return 0;
}