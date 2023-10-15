# Входные данные
strs = ["a"]

# Решение
strs2 = []
res = []
res2 = []

for i in strs:
    strs2.append(sorted(i))

for i in range(len(strs)):
    if strs2[i] in res:
        continue

    res2.append([])
    for j in range(i, len(strs)):
        if strs2[i] == strs2[j]:
            res2[len(res2)-1].append(strs[j])
            if strs[i] not in res:
                res.append(strs2[i])
print(res2)