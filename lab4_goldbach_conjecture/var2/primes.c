#include <stdio.h>
#include "calculate_primes.h"

/* Реализация Решета Эратосфена */
void calculate_primes(int primes[], long number) {
  long i, k;
  primes[0] = 0;
  primes[1] = 0;
  /* Сначала берём все числа от 2-ч до number */
  for ( i = 2; i <= number; i++)
    primes[i] = 1;
  k = 2;
  /* Просеиваем числа */
  while ( k*k <= number ) {
    if ( primes[k]) {
      i = k*k;
      while ( i <= number ) {
	primes[i] = 0;
	i += k;
      }
    }
    k ++;
  }
}
