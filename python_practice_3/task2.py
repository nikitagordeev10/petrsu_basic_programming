# Входные данные
num1 = "456"
num2 = "123"

# Решение
res1 = res2 = 0

for i in range(len(num1)):
    res1 += (ord(num1[i])-48) * 10 **(len(num1)-i-1)
for i in range(len(num2)):
    res2 += (ord(num2[i])-48) * 10 **(len(num2)-i-1)

print(res1*res2)