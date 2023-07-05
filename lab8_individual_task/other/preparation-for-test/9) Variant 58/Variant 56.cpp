#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>

int main() {
	int a = 165, b = 255, c;
	do {
		c = a > b ? a - b : b - a;
		if (a > b) a = c; else b = c;
	} while (a != b);
	printf("%d", a);
}