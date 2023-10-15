import statistics
from math import ceil


# Принимает путь к файлу и возвращает список строк этого файла
def read_data_from_file(path):
    data = list()
    with open(path, "r") as file:
        for line in file:
            data.append(line)
    return data


# Принимает список строк и интервал и возвращает список списков данных, разделённые по заданному интервалу
def split_data(data, interval):
    segments = list()
    current_segments = list()
    current_time = float(data[1].split(',')[0])

    for i in range(1, len(data)):
        current_string = data[i]

        time, count = map(float, current_string.split(','))

        if (time - current_time) <= (interval * 60.0):
            current_segments.append([time, count])
        else:
            segments.append(current_segments)
            current_segments = list()
            current_segments.append([time, count])
            current_time = time

    segments.append(current_segments)
    return segments


# Принимает список значений и возвращает статистику по этому списку
def calculate_statistics(segments):
    stats = dict()
    stats["Начало интервала"] = ceil((segments[0][0]) / 60)
    stats["Конец интервала"] = ceil((segments[len(segments) - 1][0]) / 60)
    stats["Количество значений:"] = len(segments)
    stats["Среднее значение:"] = statistics.mean(segments[1])
    stats["Мода:"] = statistics.mode(segments[1])
    stats["Медиана:"] = statistics.median(segments[1])
    return stats


# Читаем файл
file = "correct-values.csv"  # input()
interval = 5  # int(input())
data = read_data_from_file(file)

# Делим данные на отрезки с заданным интервалом
segments = split_data(data, interval)

# Для каждого отрезка считаем и выводим статистику
for i in range(len(segments)):
    stats = calculate_statistics(segments[i])
    print(stats)
