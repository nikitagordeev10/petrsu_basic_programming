#include <stdio.h>
#include "calculate_primes.h"

int primes[10000001];

int main() {
  int first, last;
  int decomposition = 0;
  int x = 0;
  int y = 0;
  int i, j;

  printf("Введите 2 чётных числа: ");
  scanf("%d %d", &first, &last);

  for (i = 0; i <= last; i++) primes[i] = 1;

  /* 0 и 1 - не простые числа */
  primes[0] = 0;
  primes[1] = 0;

  calculate_primes(primes, last);

  /*Проверка: можно ли разложить четное число на сумму 2 простых. */
  for (i = first; i <= last; i += 2) {
    
    /* Проверим что j простое число и i - j тоже простое число*/
    for (j = 2; j * 2 <= i; j++) {
      if (primes[j] == 1 && primes[i - j] == 1) {
	decomposition++;
	
	/*берём первое возможное разложение числа на 2 простых */  
	  if (x == 0) {
	    x = j;
	    y = i - j;
	  }
      }
    }
    
    /*Выведем четное число, количество его разложений на 2 простых, и 2 чис*/
    printf("%d %d %d %d \n", i, decomposition, x, y);

    /* Обнулим все значения для следующего числа*/
    decomposition = 0;
    x = 0;
    y = 0;
  }
  return 0;
}
