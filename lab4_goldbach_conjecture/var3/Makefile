all: primes goldbach

goldbach: goldbach.o calculate_primes.o
	gcc -g -O0 -o goldbach goldbach.o calculate_primes.o

primes: primes.o calculate_primes.o
	gcc -g -O0 -o primes primes.o calculate_primes.o


goldbach.o: goldbach.c calculate_primes.h
	gcc -g -O0 -c goldbach.c

primes.o: primes.c calculate_primes.h
	gcc -g -O0 -c  primes.c

calculate_primes.c: calculate_primes.c calculate_primes.h
	gcc -g -O0 -c calculate_primes.c

clean:
	rm primes *.o
	rm goldbach *.o
