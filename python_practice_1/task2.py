# Входные данные
nums = [4, -1, 7, 0, 1, 2, -1, 5]
S = 3

# Решение
def SumSetsS(sum, numbers):
    SumSetsS_buf = []
    for i in range(len(numbers)):
        sum -= numbers[i]
        SumSetsS_buf.append(numbers[i])
        if sum == 0:
            return SumSetsS_buf

real_res = []
for i in range(len(nums)):
    main_buf = SumSetsS(S, nums[i:])
    if main_buf != None:
        real_res.append(main_buf)
print(real_res)