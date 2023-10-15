#include "calculate_primes.h" 


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
