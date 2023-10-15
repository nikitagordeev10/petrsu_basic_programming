# Входные данные
n = 10

# Решение
def PrimeDivisor(num):
    # Делим на 5 пока нет остатка
    while num % 5 == 0:
        num //= 5
    # Делим на 3 пока нет остатка
    while num % 3 == 0:
        num //= 3
    # Делим на 2 пока нет остатка
    while num % 2 == 0:
        num //= 2

    return num

count = 0
i = 1
answer = []

while count < n:
    res = PrimeDivisor(i)
    if res == 1:
        count += 1
        answer.append(i)
    i += 1

print(answer)
print(i-1)