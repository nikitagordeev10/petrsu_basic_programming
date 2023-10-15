# Входные данные
n = 13

# Решение
def SumSquares(fsum, froot, res = []):
    global results

    for i in range(froot, 1, -1):
        fsum1 = fsum - i ** 2 #сумма после вычитания большего
        froot1 = int(fsum1**(1/2)) #оставшаяся сумма корень
        if fsum <= 1:
            res.clear()
            break

        if fsum1 == 0 or fsum == 0:
            res.append(i)
            res.sort()
            if res not in results:
                results.append(res)
            return 1

        else:
            res.append(i)
            # print(res,i, summ, summ1, r)
            SumSquares(fsum1, froot1, res.copy())
            res.clear()
    return 0

results = []
root = int(n**(1/2))

SumSquares(n, root)
if len(results) == 0:
    print("-1")
else:
    for i in range(len(results)):
        print(results[i])