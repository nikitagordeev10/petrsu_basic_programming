#include <stdio.h>
 
void calculate_primes(int primes[], int n);
 
int primes[100000001];
 
int main(){
 
  int n;
  printf("введите до какого значения вывести простые числа: ");
  scanf("%d", &n);
 
  calculate_primes(primes, n);
 
  for (int i = 1; i <= n; i++){
    if (primes[i]){
      printf("%d\n", i);
    }
  }
 
  return 0;
}
 
void calculate_primes(int primes[], int n){
 
  for (int i = 2; i <= n; i++){
    primes[i] = 1;
  }
 
  for (int i = 2; i <= n; i++){
    if (!primes[i]){
      continue;
    }
 
    for (int j = i+i; j <= n; j += i){
      primes[j] = 0;
    }
  }
 
}
