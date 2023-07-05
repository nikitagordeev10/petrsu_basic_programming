/* Гордеев Никита; Вариант 3; № 3 — Проверка корректности формулы суммы степенного ряда; Задача 1231
 * degreeseries.c — проверка корректности ln((1−x)/(x+1)) */

#include <math.h>
#include <stdio.h>

int main() {

    double epsilon, x; // epsilon - число вводимое пользователем
    
    // Получение чисел
    printf("Введите число X, с уловием, что |X| < 1: ");
    scanf("%lf", &x);
    printf("Введите число E, отвечающее за разность между двумя последовательными элементами ряда по абсолютному значению: ");
    scanf("%lf", &epsilon);
    
    double sum = 0, degree = 1, n = x, prev = 0; // prev - предыдущий элемент
    
    // Поиск значения естественным суммированием
    do {
        prev = n / degree;
        sum += n / degree;
        degree += 2;
        n *= x*x;
    } while (fabs(prev - (n / degree)) > epsilon); // fabs - модуль
    
    // Вывод обоих результатов с точностью в шесть знаков после запятой
    printf("Значение естественным суммированием: %.6f\n", sum * 2);
    printf("Значение с помощью формулы: %.6f\n", log((1 + x) / (1 - x)));
    
    return 0;
}
