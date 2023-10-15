import statistics
from math import ceil
from pathlib import Path


# Принимает путь к файлу и возвращает список строк этого файла
def read_data_from_file(path):
    try:
        data = list()
        with open(path, "r") as file:
            for line in file:
                data.append(line)
        return data
    except:
        if Path(path).suffix != '.csv':
            return ["Не csv не файл"]
        else:
            return ['Проблемы с файлом']


# Принимает список строк и интервал и возвращает список списков данных, разделённые по заданному интервалу
def split_data(data, interval):
    try:
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
    except:
        return ['Проблемы с файлом']


# Принимает список значений и возвращает статистику по этому списку
def calculate_statistics(segments):
    try:
        stats = dict()
        data = list()
        for curr in segments:
            data.append(curr[1])

        stats["Начало интервала"] = ceil((segments[0][0]) / 60)
        stats["Конец интервала"] = ceil((segments[-1][0]) / 60)
        stats["Количество значений:"] = len(segments)
        stats["Среднее значение:"] = statistics.mean(data)
        stats["Мода:"] = statistics.mode(data)
        stats["Медиана:"] = statistics.median(data)
        return stats
    except:
        if segments[0] is not float:
            return ['Данные не заданного типа']
        else:
            return ['Проблемы с файлом']


# Читаем файл
file = "csv-test-files/correct-values.csv"  # input()
interval = 5  # int(input())
data = read_data_from_file(file)

# Делим данные на отрезки с заданным интервалом
segments = split_data(data=data, interval=interval)
# Для каждого отрезка считаем и выводим статистику
for i in range(len(segments)):
    stats = calculate_statistics(segments[i])
    print(stats)
