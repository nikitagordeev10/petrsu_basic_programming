/* Решето Эратосфена */

void primes(char prime[], int n) {
    for (int i = 2; i < n; i++)
        prime[i] = 1;
    
    for (int i = 2; i < n; i++) {
        if (prime[i] == 0) continue;
        for (int j = i * i; j < n; j+= i) {
            prime[j] = 0;
        }
    }
}