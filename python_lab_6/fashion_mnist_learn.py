from tensorflow.keras.datasets import fashion_mnist  # набор fashion MNIST
from tensorflow.python.keras.models import Sequential  # модуль работы с сетью
from tensorflow.python.keras.layers import Dense  # полносвязные слои
from tensorflow.python.keras.layers import Dropout  # динамическое переключение
from tensorflow.python.keras.utils.np_utils import to_categorical  # работа с данными
from tensorflow.python.keras.callbacks import TensorBoard  # качество обучения
import os, time

os.environ['CUDA_VISIBLE_DEVICES'] = "0"


def main():
    # Время начала обучения сети
    start_time = time.time()

    # Загрузка набора fashion MNIST. x_train - 60000 изображений, y_train - их номера классов. x_test - 10000
    (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
    print("x_train shape:", x_train.shape, "y_train shape:", y_train.shape)

    # двумерное изображение в плоский массив
    x_train = x_train.reshape(60000, 784)
    x_test = x_test.reshape(10000, 784)

    # нормализуем интенсивность пикселей [0;1]
    x_train = x_train / 255
    x_test = x_test / 255

    # Преобразуем данные к категориальному представлению 0 - [1,0,0...]
    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)

    # ================================== Увеличить число нейронов первом слое. Сделать сеть глубокой

    # Создадим описанную модель
    model = Sequential()

    # 784 нейрона, relu -функция активации
    model.add(Dense(784, input_dim=784, activation="relu"))
    model.add(Dropout(0.2))

    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.2))

    model.add(Dense(10, activation="softmax"))

    # ================================== Выбрать наилучший оптимизатор
    # https://ru-keras.com/optimizer/ - SGD, RMSprop, Adagrad, Adadelta, Adam, Adamax, Nadam

    # Компиляция сети. Информация о нашей модели. История изменений параметров сети, подробная архитектура сети
    model.compile(loss="categorical_crossentropy",
                  optimizer="SGD",
                  metrics=["accuracy"])
    model.summary()
    callback = [TensorBoard(log_dir='logs',
                            histogram_freq=1,
                            write_images=True)]

    # ================================== Изменить количество эпох. Изменить объем мини-выборки.

    # Обучение модели
    model.fit(x_train,  # данные для обучения
              y_train,  # ответы
              batch_size=10,  # после рассчитывается функция ошибки, вычисляется градиент и корректируются веса
              epochs=100,  # обучение сети на всем наборе данных только 1 раз
              verbose=1,  # вывод отладочной информации и прогресса
              validation_split=0.2,  # разделяет выборку x_train и y_train на тренировочную и проверочную
              callbacks=callback)  # как меняются параметры

    callback = [TensorBoard(log_dir='new_logs',  # путь куда
                            histogram_freq=1,  # частота в эпохах
                            write_images=True)]  # визуализация в изображения

    # Сохранение обученной модели
    model.save("fashion_model_nikita_5_probe.h5")

    # Оценка качества работы сети
    score = model.evaluate(x_test, y_test, verbose=1)
    print("Accuracy on test data is", score[1] * 100, "percent")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
