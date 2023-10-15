import ctypes

lib = ctypes.CDLL('./primes.so')                                        # Загрузка библиотеки

lib.primes.restype = ctypes.c_voidp		                               	# Указываем, что функция возвращает void
lib.primes.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.c_int]		# Указываем, что функция принимает аргумент char *, int

N = 10000									                            # Длина набора простых чисел
Primes = (ctypes.c_char * N)()      	                            	# Создание массива из 10000 байтов
lib.primes(Primes, N) 							                        # Является ли индекс простым числом

print("Введите диапазон 4 <= N, M < 10 000 000, N < M: ")
n, m = map(int, input().split())

for num in range(n, m + 1, 2):
    print('Число:', num, end=' ')
    simple_x = 1000000
    simple_y = 0
    count = 0

    for i in range(2, num // 2 + 1):
        if ord(Primes[num - i]) == 1:		                       		# простое
            count += 1
            if simple_x > i:
                simple_x = i
                simple_y = num - i

    print('количество разложений:', count, 'пара простых чисел:', simple_x, simple_y)

