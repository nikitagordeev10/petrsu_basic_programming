#include <stdio.h>
#include <string.h>
#define _USE_MATH_DEFINES
#include <math.h>
#pragma warning(disable : 4996)

// Task 1
/*
int main() {
	/// Task
	int x = 68, y = 42, z;
	z = (x % 10 + y / 10) * 10 - x % y + x / y + 1;
	printf("%o %x %d", x, y, z);
	
	/// Decision
	// z = (x % 10 + y / 10) * 10 - x % y + x / y + 1;
	// 1) x % 10 = 68 % 10 = 8
	// 2) y / 10 = 4
	// 3) x % 10 + y / 10 = 12
	// 4) (x % 10 + y / 10) * 10 = 120
	// 5) x % y = 26
	// 6) x / y = 1
	// 7) (x % 10 + y / 10) * 10 - x % y + x / y + 1 = 120 - 26 + 1 + 1
	// ans z = 96
	// ans x → 8сс  = 104
	// ans y → 16cc = 1A
	
	/// Answer
	// 104 2A 96
}
*/

// Task 2
/*
int main() {
	/// Task
	double x = M_PI, y = 90.692;
	printf("x%4.2lfy%3.1lfy+x", y, x);

	/// Decision
	// x(%4.2lf)y(%3.1lf)y+x
	// x 90.69 y 3.1 y + x

	/// Answer
	// x90.69y3.1y+x
}
*/

// Task 3
/*
int main() {
	/// Task
	int a = 43, b = 44, c = 97, d = 62, s;
	d += (a++) + (++b) % (c--) - (--a);
	printf("%d %d %d %d", a, b, c, d);

	/// Decision
	// 1) (++b) % (c--) = 45 % 97 = 45; b = 45; c = 96;
	// 2) (a++) + (++b) % (c--) = 43 + 45 = 88; a = 44; b = 45; c = 96;
	// 3) (a++) + (++b) % (c--) - (--a) = 88 - 43 = 45; a = 43; b = 45; c = 96;
	// 4) d = 45 + 62 = 107;

	/// Debug
	// s = (++b) % (c--); // s = 45
	// printf("%d", s);

	/// Answer
	// 43 45 96 107
}
*/

// Task 4
/*
int main() {
	/// Task
	int a = 90, b = 15, c = 66, d;
	d = a > b ? b < c ? b : c : a;
	printf("%d", d);

	/// Decision
	// d = (a > b) ? (b < c ? (b) : (c)) : a;
	// 1) b < c → 15
	// 2) a > b → 15

	/// Answer
	// 15
}
*/

// Task 5
/*
int main() {
	/// Task
	char s[20] = "jvjyaytcmfxxf";
	strcat(s, "pdmef");
	s[16] = '\0';
	printf("%s", s + 6);

	/// Decision
	//				 0  1  2  3  4  5  6  7  8  9  10 11 12
	// char s[20] = "j  v  j  y  a  y  t  c  m  f  x  x  f";
	//
	// 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17
	// j  v  j  y  a  y  t  c  m  f  x  x  f  p  d  m  e  f
	// 
	// 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 
	// j  v  j  y  a  y  t  c  m  f  x  x  f  p  d  m  
	//
	// t  c  m  f  x  x  f  p  d  m

	/// Answer
	// 6  7  8  9  10 11 12 13 14 15
	// t  c  m  f  x  x  f  p  d  m

}
*/

// Task 6
/*
int main() {
	/// Task
	int a = 19, b = 53, c = 19, d = 16;
	d = a & b + b | c + c ^ d;
	printf("%d", d);

	/// Decision
	// d = (a & (b + b)) | ((c + c) ^ d);
	// 1) b + b = 106; 
	// 2) c + c = 38;
	// 3) a & (b + b) = 2;
	// 4) (c + c) ^ d = 54;
	// 5) 54

	/// Debug
	// int s1;
	// s1 = c + c ^ d;
	// printf("%d", s1);

	/// Answer
	// 54
}
*/

// Task 7
/*
int main() {
	/// Task
	int a = 80, b = 78;
	int* p1 = &a, * p2 = &b;
	*p2 = *p2 + (*p1 = *p2 + b) % a;
	printf("%d, %d", a, b);

	/// Decision
	// 1) a = (*p1 = *p2 + b) → a = 156
	// 2) *p2 = *p2 + ((*p1 = *p2 + b) % a) = 78 + (156 % 156) = 78 + 0 = 78 → b = 78

	/// Answer
	// 156 78
}
*/

// Task 8
/*
int main() {
	/// Task
	int a[10] = { 0, 2, 6, 7, 3, 8, 9, 4, 5, 1 }, i, t;
	t = a[1];
	for (i = 1; i < 9; i++)
		a[i] = a[i + 1];
	a[9] = t;
	t = a[8];
	for (i = 8; i > 1; i--)
		a[i] = a[i - 1];
	a[1] = t;
	for (i = 0; i < 10; i++)
		printf("%d%c", a[i], (i < 9) ? ('+') : ('!'));

	/// Decision
	// i = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
	// a = 0, 2, 6, 7, 3, 8, 9, 4, 5, 1 
	// 
	// t = 2;
	// 
	// i = 1, 2, 3, 4, 5, 6, 7, 8, 9
	// a = 6, 7, 3, 8, 9, 4, 5, 1, 2
	// 
	// t = 1;
	// 
	// i = 8, 7, 6, 5, 4, 3, 2, 1
	// a = 5, 4, 9, 8, 3, 7, 6, 1
	// 
	// i = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
	// a = 0, 1, 6, 7, 3, 8, 9, 4, 5, 2 

	///Answer
	// 0+1+6+7+3+8+9+4+5+2!
}
*/

// Task 9
/*
int main() {
	/// Task
	int a[10] = { 5, 9, 0, 4, 8, 3, 2, 7, 1, 6 }, s = 0;
	int i;
	for (i = 0; i < 10; i++) {
		if ((a[i] - a[0]) < 5 == (a[i] - a[9]) > 5)
			s += a[i];
	}
	printf("%d", s);

	/// Decision
	// i = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
	// a = 5, 9, 0, 4, 8, 3, 2, 7, 1, 6 
	// 
	// i = 0
	// ((5 - 5) < 5 == (5 - 5) > 5)
	// s = 0 → т.к. числа >= 11 нет в списке, то s = 0

	/// Answer
	// 0
}
*/

// Task 10
/*
int main() {
	/// Task
	int a[10] = { 7, 5, 0, 2, 4, 1, 9, 8, 6, 3 };
	int* p = a;
	*p = *(p + 4); p += 5; *p += *(p - 5);
	for (p = a; p < a + 10; p++)
		printf("%d", *p);*

	/// Decision
	// i = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
	// a = 7, 5, 0, 2, 4, 1, 9, 8, 6, 3
	// *p = *(p + 4);  // *p = 4;
	// p += 5; // p = 5
	// *p += *(p - 5); // 4

	///// Debug
	////            0, 1, 2, 3, 4, 5, 6, 7, 8, 9
	//int a[10] = { 7, 5, 0, 2, 4, 1, 9, 8, 6, 3 }, d;
	//int *p = a; // *p = 7
	//*p = *(p + 4); // *p → a[0] = a[4] = 4 → 
	//p += 5; // *p = 1
	//d = *(p - 5); // d = a[0] = 4
	//*p += d; //*p = 5
	//for (p = a; p < a + 10; p++)
	//	printf("%d", *p); 

	/// Answer
	// i        = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
	// true_ans = 4, 5, 0, 2, 4, 5, 9, 8, 6, 3
	// my_ans   = 4  5  0  2  4  5  9  8  6  3
}
*/

// Task 11
/*
int main() {
	/// Task
	int a[10] = { 7, 8, 1, 5, 3, 0, 4, 9, 2, 6 }, s = 0;
	int i;
	for (i = 1; i < 9; i++) { // 1 2 3 4 5 6 7 8
		if (a[i] < (a[i - 1] + a[i + 1]) / 2)
			continue;
		s += a[i];
	}
	printf("%d", s);
	
	/// Decision
	// (a[i] < ((a[i - 1] + a[i + 1]) / 2))
	// 
	// i = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
	// a = 7, 8, 1, 5, 3, 0, 4, 9, 2, 6
	// 
	// i = 1, 8 < ((7 + 1)) / 2) → 8 < 4 → s = 8 !!!
	// i = 2, 1 < ((8 + 5)) / 2) → 1 < 6 → s = 8
	// i = 3, 5 < ((1 + 3)) / 2) → 5 < 2 → s = 13 !!!
	// i = 4, 3 < ((5 + 0)) / 2) → 3 < 2 → s = 16 !!!
	// i = 5, 0 < ((3 + 4)) / 2) → 0 < 3 → s = 16
	// i = 6, 4 < ((0 + 9)) / 2) → 4 < 4 → s = 20 !!!
	// i = 7, 9 < ((4 + 2)) / 2) → 9 < 3 → s = 29 !!!
	// i = 8, 2 < ((9 + 6)) / 2) → 2 < 7 → s = 29
	
	/// Answer
	// 29
}
*/

// Task 12
/*
int main() {
	/// Task
	char a[20] = "jcnbmfaqncwm";
	int i;
	for (i = 2; i < 7; i++) {
		a[i] = a[i + 3];
	}
	printf("%s", a);

	/// Decision
	// 0  1  2  3  4  5  6  7  8  9  10 11 
	// j  c  n  b  m  f  a  q  n  c  w  m
	//
	// 2  3  4  5  6 
	// f  a  q  n  c 
	//
	// 0  1  2  3  4  5  6  7  8  9  10 11 
	// j  c  f  a  q  n  c  q  n  c  w  m

	/// Answer
	// jcfaqncqncwm
}
*/

// Task 13
/*
int main() {
	/// Task
	int a[4][4] = {
		{ 0, 1, 2, 3 },
		{ 5, 6, 4, 7 },
		{ 10, 11, 9, 8 },
		{ 12, 15, 14, 13 }
	}, s = 0, i, j;
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			if (i + j < 4) printf("%d", a[i][j]);
		}
	}

	/// Decision
	// a[0][0] — 0
	// a[0][1] — 1
	// a[0][2] — 2
	// a[0][3] — 3
	// a[1][0] — 5
	// a[1][1] — 6 
	// a[1][2] — 4
	// a[1][3] — 7
	// a[2][0] — 10
	// a[2][1] — 11
	// a[2][2] —
	// a[2][3] — 
	// a[3][0] — 12
	// a[3][1] — 
	// a[3][2] —
	// a[3][3] — 

	/// Answer
	// 0123564101112
}
*/

// Task 14
/*
int main() {
	/// Task
	int x = 25;
	switch (x) {
	case 24: printf("%d", x);
	case 25: printf("%d", x + 1);
	case 26: printf("%d", x - 1);
	}

	/// Answer
	// 2624
}
*/

// Task 15
/*int main() {
	/// Task
	int s = 0, i = 7;
	while (1) {
		s += i;
		if (s > 100) break;
		i += i;
	}
	printf("%d %d", i, s);
	
	/// Decision
	// (1) s = 7; i = 14;
	// (2) s = 21; i = 28;
	// (3) s = 49; i = 56;
	// (4) s = 105; i = 56

	/// Answer
	// 56 105
}
 */

// Task 16
int main() {
	/// Task
	int a = 84, b = 204, c;
	do {
		c = (a > b) ? (a - b) : (b - a);
		if (a > b) a = c; else b = c;
	} while (a != b);
	printf("%d", a);

	/// Decision
	// (1) c = b - a = 204 - 120;	→ a = 84; b = 120; c = 120;
	// (2) c = b - a = 120 - 84;	→ a = 84; b = 36; c = 36;
	// (3) c = a - b = 84 - 36;		→ a = 48; b = 36; c = 36;
	// (4) c = a - b = 48 - 36;		→ a = 12; b = 36; c = 12; 
	// (5) c = b - a = 36 - 12;		→ a = 12; b = 24; c = 24;
	// (6) c = b - a = 24 - 12;		→ a = 12; b = 12; c = 12;
	
	/// Answer
	// 12
}