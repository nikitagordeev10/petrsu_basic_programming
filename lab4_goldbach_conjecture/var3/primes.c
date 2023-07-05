#include <stdio.h>
#include "calculate_primes.h"
 
int primes[100000001];
 
int main(){
 
  int n;
  printf("Введите до какого значения вывести простые числа: ");
  scanf("%d", &n);
 
  calculate_primes(primes, n);
 
  for (int i = 1; i <= n; i++){
    if (primes[i]){
      printf("%d\n", i);
    }
  }
 
  return 0;
}
 

