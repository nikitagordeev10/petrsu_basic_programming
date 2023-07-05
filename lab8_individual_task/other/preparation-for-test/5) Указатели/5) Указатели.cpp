﻿#include <stdio.h>
#include <stdarg.h>

int sum(int n, ...) {
    int result = 0;
    va_list factor;         //указатель va_list
    va_start(factor, n);    // устанавливаем указатель
    for (int i = 0;i < n; i++) {
        result += va_arg(factor, int);  // получаем значение текущего параметра типа int
    }
    va_end(factor); // завершаем обработку параметров
    return result;
}

int main(void) {
    printf("%d \n", sum(4, 1, 2, 3, 4));
    printf("%d \n", sum(5, 12, 21, 13, 4, 5));
    return 0;
}
