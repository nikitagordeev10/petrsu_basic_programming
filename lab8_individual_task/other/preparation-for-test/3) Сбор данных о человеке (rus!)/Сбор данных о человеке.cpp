#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
struct date {
    int day;
    char month[20];
    int year;
};
struct persone {
    char firstname[20];
    char lastname[20];
    struct date bd;
};
int main() {
    system("chcp 1251");
    system("cls");
    struct persone p;
    printf("Введите имя : ");
    scanf("%s", p.firstname);
    printf("Введите фамилию : ");
    scanf("%s", p.lastname);
    printf("Введите дату рождения\nЧисло: ");
    scanf("%d", &p.bd.day);
    printf("Месяц: ");
    scanf("%s", p.bd.month);
    printf("Год: ");
    scanf("%d", &p.bd.year);
    printf("\nВы ввели : %s %s, дата рождения %d %s %d года",
        p.firstname, p.lastname, p.bd.day, p.bd.month, p.bd.year);
    
    return 0;
}