#include <stdio.h>

int main()
{
    struct student
    {
        int num = 10;
    } var;

    printf("%d", var.num);
}