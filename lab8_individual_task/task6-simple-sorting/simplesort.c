/* Гордеев Никита; Вариант 3; № 6 — Простые сортировки; Задача Array112;
 * simplesort.c — Упорядочивание элементов массива «пузырьковой» сортировкой */

#include <stdio.h>
#include <stdlib.h>

int main() {

    int *arr; int n; int done = 0;
    
    printf("Введите длину массива: ");
    scanf("%d", &n);

    if (n > 100) {
        printf("Введено число превосходящее 100, используйте число поменьше");
    	exit;
    }    
    
    else {    
        arr = malloc(n*sizeof(int));
    
        printf("Введите элементы массива: ");
        int sum = 0;
        for (int i = 0; i < n; i++) {
            scanf("%d", arr + i);
            sum += arr[i];
        }

	// Проверка суммы элементов на превосхождение 1000 (по условию)  
	if (sum > 1000) {
            printf("Сумма введённых чисел по абсолютному значению превосходит 1000, используйте числа поменьше");
            exit;
        }    
        
        else {
	    // Пузырьковая сортировка
            while (!done) {
                done = 1;

	        // Повтор действий n-1 раз
                for (int i = 0; i < n - 1; i++) {

		    // Сравнение соседних элементов
                    if (arr[i] > arr[i + 1]) {

                        done = 0;

		        // Перемена их местами, если левый элемент пары больше правого
                        int t = arr[i];
                        arr[i] = arr[i + 1];
                        arr[i + 1] = t;
                    }
                }
            }
            printf("Отсортированный массив: ");
            for (int i = 0; i < n; i++) {
                printf("%d ", arr[i]);
            }
        }
    }
    
    printf("\n");
    
    return 0;
}
