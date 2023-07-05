#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int fib(int x) {
    if (x == 0) 
        return 0;

    if (x == 1)
        return 1;

    return fib(x - 1) + fib(x - 2);
}

int main()
{
    int N;
    printf("N=");
    scanf("%d", &N); // вводим число N
    for (int i = 1; i <= N; i++) // В цикле выводим N чисел Фибоначчи
        printf("%d ", fib(i));
    getchar(); getchar();
    return 0;
}