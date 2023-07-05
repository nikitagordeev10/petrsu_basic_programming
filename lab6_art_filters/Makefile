filter: filter.o bmp_io.o bmp_motion.o
	gcc -g -O0 -o filter filter.o bmp_io.o bmp_motion.o

filter.o: filter.c bmp.h
	gcc -g -O0 -c -Wall -Wextra filter.c

bmp_motion.o: bmp_motion.c bmp.h
	gcc -g -O0 -c -Wall -Wextra bmp_motion.c

bmp_io.o: bmp_io.c bmp.h
	gcc -g -O0 -c -Wall -Wextra bmp_io.c
	
clean:
	rm -rf *.o filter

