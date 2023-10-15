# Входные данные
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

# Решение
def word_search(i, j, counter):
    global flag_matrix, board, word, n, m
    word_len = len(word)
    if counter == word_len:
        return True

    flag = False

    if i + 1 < m and flag_matrix[i + 1][j] == 1 and board[i + 1][j] == word[counter]:
        flag = word_search(i + 1, j, counter + 1)
        if flag:
            return flag

    if i - 1 >= 0 and flag_matrix[i - 1][j] == 1 and board[i - 1][j] == word[counter]:
        flag = word_search(i - 1, j, counter + 1)
        if flag:
            return flag

    if j + 1 < n and flag_matrix[i][j + 1] == 1 and board[i][j + 1] == word[counter]:
        flag = word_search(i, j + 1, counter + 1)
        if flag:
            return flag

    if j - 1 >= 0 and flag_matrix[i][j - 1] == 1 and board[i][j - 1] == word[counter]:
        flag = word_search(i, j - 1, counter + 1)
        if flag:
            return flag

    flag_matrix[i][j] = 0
    return False


flag_matrix = []

m = 3
n = 4
res = False

for i in range(m):
    flag_matrix.append([])
    for j in range(n):
        flag_matrix[i].append(1)

for i in range(m):
    for j in range(n):
        if board[i][j] == word[0]:
            if word_search(i, j, 1):
                res = True

print(res)