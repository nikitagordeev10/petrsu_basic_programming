# Входные данные
strs = ["flower", "flow", "flight"]

# Решение
j = -1
flag = True
res = ""

while flag:
    j += 1
    if len(strs[0]) <= j:
        break

    symbol = strs[0][j]
    for i in strs:
        # размер слова
        if len(i) <= j:
            flag = False
            break
        # префикс
        if i[j] != symbol:
            flag = False
            break

    if flag:
        res += symbol

print(res)
