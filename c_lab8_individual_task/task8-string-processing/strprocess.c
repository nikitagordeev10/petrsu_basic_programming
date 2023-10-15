/* Гордеев Никита; Вариант 3; № 8 — Обработка строк; Задача String36;
 * strprocess.c — Даны строки S, S1 и S2. Заменить в строке S первое вхождение строки S1 на строку S2 */

#include <stdio.h>
#include <string.h>

int main() {
    char s[256] = "", 
    s1[256] = "", 
    s2[256] = "", 
    s3[256] = "";
    
    printf("Введите 3 строки: ");
    scanf("%s %s %s", s, s1, s2);
    

    char *found = strstr(s, s1); // функция strstr ищет первое вхождение подстроки s1 в строке s
    if (found) {
        strncpy(s3, s, found - s); // функция strncpy копирует первые found - s символов из строки s в строку s3
        strcpy(s3 + (found - s), s2); //  функция strcpy копирует Си-строку s2 включая завершающий нулевой символ в строку назначения
        if (strlen(found) > strlen(s1)) strcpy(s3 + strlen(s3), found + strlen(s1)); // функция strlen - длина строки; 
        printf("%s\n", s3);
    }
    
    else printf("%s\n", s);
    return 0;
}
