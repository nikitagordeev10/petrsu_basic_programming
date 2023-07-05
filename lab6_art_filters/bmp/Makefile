filter: filter.o bmp_io.o bmp_gray.o
	gcc -o filter filter.o bmp_io.o bmp_gray.o

filter.o: filter.c bmp.h
	gcc -c -Wall -Wextra filter.c

bmp_gray.o: bmp_gray.c bmp.h
	gcc -c -Wall -Wextra bmp_gray.c

bmp_io.o: bmp_io.c bmp.h
	gcc -c -Wall -Wextra bmp_io.c
	
clean:
	rm -rf *.o filter

