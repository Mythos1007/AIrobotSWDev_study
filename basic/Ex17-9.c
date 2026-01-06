#include <stdio.h>

struct list
{
    int num;
    struct list *next;
};

int main()
{
    struct list a = {10, NULL};
    struct list b = {20, NULL};
    struct list c = {30, NULL};
    struct list *head = &a, *current;

    a.next = &b;
    b.next = &c;

    printf("head->num : %d\n", head->num);
    printf("head->next->num : %d\n", head->next->num);
    printf("list all : ");
    current = head;
    while (current != NULL)
    {
        printf("%d ", current->num);
        current = current->next;
    }
printf("\n");

return 0;
}