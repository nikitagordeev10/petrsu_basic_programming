# Входные данные
null = None
wood = [1, 2, 3, null, 4]


# Решение
def step_to_leaf(index, way):
    global wood
    lenght = len(wood)

    if 2 * index - 1 >= lenght:
        print(way)
        return way
    # Проверка на конец левой и правой ветки
    if wood[2 * index - 1] == None and wood[2 * index] == None:
        print(way)
        return way

    # Спуск по левой ветке
    if wood[2 * index - 1] != None:
        way.append(wood[2 * index - 1])
        wood[2 * index - 1] = null
        step_to_leaf(index + 1, way.copy())
        way.pop()

    # Спуск по правой ветке
    if wood[2 * index] != None:
        way.append(wood[2 * index])
        wood[2 * index] = null
        step_to_leaf(index + 2, way.copy())


if len(wood) > 0:
    way = [wood[0]]
else:
    print("Нет ветвей")
    exit()

step_to_leaf(1, way)
