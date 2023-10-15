from main import *
import unittest


class ProcessingCsvFile(unittest.TestCase):

    # Тест 1 - нет файла
    def test_no_file(self):
        result = read_data_from_file("")
        self.assertEqual(result, ['Не csv не файл'])

    # Тест 2 - нет прав на чтение
    def test_no_reading_rights(self):
        result = read_data_from_file("csv-test-files/no-reading-rights.csv")
        self.assertEqual(result, ['Проблемы с файлом'])

    # Тест 3 - не csv файл
    def test_no_csv_format(self):
        result = read_data_from_file("csv-test-files/no-csv-format.jpg")
        self.assertEqual(result, ['Не csv не файл'])

    # Тест 4 - в какой-то из строк файла только одна колонка;
    def test_one_column(self):
        data = read_data_from_file("csv-test-files/one-column.csv")
        segments = split_data(data, 5)
        self.assertEqual(segments, ['Проблемы с файлом'])

    # Тест 5 - данные не заданного типа
    def test_invalid_type(self):
        data = read_data_from_file("csv-test-files/one-column.csv")
        segments = split_data(data, 5)
        for i in range(len(segments)):
            stats = calculate_statistics(segments[i])
            self.assertEqual(stats, ['Данные не заданного типа'])

    # Тест 6 - делится на нужные интервалы по времени
    def test_correct_intervals(self):
        data = read_data_from_file("csv-test-files/correct-values.csv")
        segments = split_data(data, 5)
        my_list = []
        for i in range(len(segments)):
            my_list.append(list(calculate_statistics(segments[i]).values()))
        correct_intervals = [my_list[0][0], my_list[0][1], my_list[1][0], my_list[1][1]]
        self.assertEqual(correct_intervals, [2, 7, 9, 10])

    # Тест 7 - количество интервалов правильное
    def test_quantity_intervals(self):
        data = read_data_from_file("csv-test-files/correct-values.csv")
        segments = split_data(data, 5)
        quantity = 0
        for i in range(len(segments)):
            quantity += 1
        self.assertEqual(quantity, 2)

    # Тест 8 - статистики подсчитываются верно
    def test_all_statistics(self):
        data = read_data_from_file("csv-test-files/correct-values.csv")
        segments = split_data(data, 5)
        my_list = []
        for i in range(len(segments)):
            stats = calculate_statistics(segments[i])
            my_list.append(stats)
        self.assertEqual(my_list, [{'Количество значений:': 4,
                                    'Конец интервала': 7,
                                    'Медиана:': 250.0,
                                    'Мода:': 100.0,
                                    'Начало интервала': 2,
                                    'Среднее значение:': 250.0},
                                   {'Количество значений:': 2,
                                    'Конец интервала': 10,
                                    'Медиана:': 550.0,
                                    'Мода:': 500.0,
                                    'Начало интервала': 9,
                                    'Среднее значение:': 550.0}]
                         )
