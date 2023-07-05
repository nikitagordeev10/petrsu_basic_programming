#include <stdio.h>

long long fib(unsigned long long a)
{
    if (a == 1 || a == 2)
        return 1;
    return fib(a - 1) + fib(a - 2);
}
int main()
{
    unsigned long long a = fib(20);
    printf("%llu \n", a);
    return 0;
}