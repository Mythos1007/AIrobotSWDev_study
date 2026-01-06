#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 100

struct biznesscard{
    int number;
    char name[MAX];
    char phone[MAX];
    char company[MAX];
    char email[MAX];
    char etc[MAX];
};
typedef struct biznesscard Biznesscard;

void ClearBuffer()
{
    int c; 
    while( (c = getchar()) != '\n' && c != EOF);
}
void GetInput(char *ch, int len)
{
    if(fgets(ch, len, stdin) != NULL)
    {
        len = strlen(ch);
        if(len > 0 && ch[len - 1] == '\n'){
            ch[len-1] = '\0';
        }
    }
}

int main()
{
    FILE *fp;
    FILE *ofp;
    Biznesscard biz[MAX];
    int res;
    int new_number = 0;
    int del_number = 0;

    printf("===========================\n");
    printf("\t미니 명함 관리 프로그램\n");
    printf("===========================\n");
    printf("1. 명함 목록 보기\n");
    printf("2. 명함 추가\n");
    printf("3. 명함 수정\n");
    printf("4. 명함 삭제\n");
    printf("5. 저장 후 종료\n");
    printf("---------------------------\n");

    fp = fopen("biznesscard.txt", "r");
    if(fp == NULL)
    {
        printf("Read Error\n");
        return 1;
    }
    int n = 0;
    while(1)
    {
        res = fscanf(fp, "%d %s %s %s %s", &biz[n].number, 
biz[n].name, biz[n].phone, biz[n].company, biz[n].email);
        fgets(biz[n].etc, sizeof(biz[n].etc), fp);
        if(res == EOF)
            break;
        n++;  
    }

    int menu = 0;
    while(1) 
    {
        printf("\n메뉴를 선택하세요 : ");
        scanf("%d", &menu);
        ClearBuffer();

        switch (menu)
        {
        case 1:
            printf("[명함 목록 보기]\n");
            fp = fopen("biznesscard.txt", "r");
            if(fp == NULL)
            {
                printf("Read Error\n");
                return 1;
            }
            n = 0;
            while(1)
            {
                res = fscanf(fp, "%d %s %s %s %s", &biz[n].number, 
biz[n].name, biz[n].phone, biz[n].company, biz[n].email);
                fgets(biz[n].etc, sizeof(biz[n].etc), fp);
                if(res == EOF)
                    break;
                n++;  
            }
            for(int i = 0; i < n; i++)
            {
                printf("%5d%10s|%20s|%20s|%25s|%30s", 
biz[i].number, biz[i].name, biz[i].phone, biz[i].company, biz[i].email, biz[i].etc);
            }
            break;
        case 2:
            printf("[명함 추가]\n");
            char name[MAX]; char phone[MAX]; char company[MAX]; char email[MAX]; char etc[MAX];
            ofp = fopen("biznesscard.txt", "a");
            printf("이름 입력 : ");         scanf("%s", name);
            printf("전화번호 입력 : ");     scanf("%s", phone);
            printf("회사 입력 : ");         scanf("%s", company);
            printf("이메일 입력 : ");       scanf("%s", email);
            printf("추가 정보 입력 : ");    scanf("%s", etc);
            fprintf(ofp, "\n%d %s %s %s %s %s", n, name, phone, company, email, etc);
            fclose(ofp);
            n++;
            break;
        case 3:
            printf("[명함 수정]\n");
            new_number = 0;
            char n_name[MAX]; char n_phone[MAX]; char n_company[MAX]; char n_email[MAX]; char n_etc[MAX];
            
            printf("수정할 명함 번호 입력 : "); 
            scanf("%d", &new_number);
            if(new_number < 0 || new_number >= n)
            {
                printf("ERROR : 명함번호 %d는 존재하지 않습니다\n", new_number);
                break;
            }
            ClearBuffer();

            printf("새 이름 입력(그대로 두려면 엔터만 입력) : ");       
            GetInput(n_name, MAX);
            if(strlen(n_name) != 0)  
                strcpy(biz[new_number].name, n_name);

            printf("새 전화번호 입력(그대로 두려면 엔터만 입력) : ");   
            GetInput(n_phone, MAX);
            if(strlen(n_phone) != 0) 
                strcpy(biz[new_number].phone, n_phone);

            printf("새 회사 입력(그대로 두려면 엔터만 입력) : ");
            GetInput(n_company, MAX);
            if(strlen(n_company) != 0) 
                strcpy(biz[new_number].company, n_company);
            
            printf("새 이메일 입력(그대로 두려면 엔터만 입력) : ");
            GetInput(n_email, MAX);
            if(strlen(n_email) != 0) 
                strcpy(biz[new_number].email, n_email);
            
            printf("새 추가 정보 입력(그대로 두려면 엔터만 입력) : ");
            GetInput(n_etc, MAX);
            if(strlen(n_etc) != 0) 
                strcpy(biz[new_number].etc, n_etc);

            ofp = fopen("biznesscard.txt", "w");
            if(ofp == NULL)
            {
                printf("Read Error\n");
                return 1;
            }
            for(int i = 0; i < n; i++)
            {
                fprintf(ofp, "%d %s %s %s %s %s", 
i, biz[i].name, biz[i].phone, biz[i].company, biz[i].email, biz[i].etc);
            }
                
            fclose(ofp);
            printf("\n=> 수정이 완료되었습니다\n");
            break;
        case 4:
            printf("[명함 삭제]\n");
            printf("삭제할 명함 번호 입력 : ");
            
            scanf("%d", &del_number);
            ClearBuffer();
            if(del_number < 0 || del_number >= n)
            {
                printf("ERROR : 명함번호 %d는 존재하지않습니다\n", del_number);
                break;
            }

            printf("정말 삭제하시겠습니까? (y/n) : ");
            char y;
            while(1)
            {
                scanf("%c", &y);
                if(y == 'y' || y == 'Y')
                {
                    // 특정 명함번호부터 하나씩 당겨서 덮어씌우면 그게 삭제임
                    for(int i = del_number; i < n-1; i++) 
                    {
                        biz[i] = biz[i+1];
                    }
                    n--; // 명함 갯수 감소

                    ofp = fopen("biznesscard.txt", "w");
                    if(ofp == NULL)
                    {
                        printf("Write Error\n");
                        break;
                    }
                    for(int i = 0; i < n; i++)
                    {
                        fprintf(ofp, "%d %s %s %s %s %s\n", 
i, biz[i].name, biz[i].phone, biz[i].company, biz[i].email, biz[i].etc);
                    }
                    fclose(ofp);
                    
                    printf("\n=> 삭제 되었습니다.]n");
                    break;
                }
                else if(y == 'n' || y == 'N')
                {
                    printf("삭제하지 않았습니다(그대로 유지)\n");
                    break;
                }
                else 
                {
                    printf("y/n으로 다시 입력하세요\n");
                }
                    
            }
            
            break;
        case 5:
            printf("저장 후 종료\n");
            exit(1);
            break;
        default:
            printf("잘못된 입력입니다\n");
            break;
        }   
    }
    

    fclose(fp);
    printf("\n");
    return 1;

}