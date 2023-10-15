numbers = [4, -1, 7, 0, 1, 2, -1, 5]
length = len(numbers)
s = set()

for i in range(length):
    for j in range(0, length):
        for k in range(0, length - 1):
            if i == j or i == k or j == k:
                continue
            if numbers[i] + numbers[j] + numbers[k] == 0:
                res = [str(numbers[i]), str(numbers[j]), str(numbers[k])]
                res.sort()
                s.add(",".join(res))
print(list(s))
