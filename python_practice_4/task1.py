# Входные данные
nums =  [-2,1,-3,4,-1,2,1,-5,4]

# Решение
sum = 0
maxs = max(nums)

for i in nums:
    sum += i

    if maxs < sum:
        maxs = sum

    if sum <= 0:
        sum = 0

print(maxs)