from tensorflow.keras.datasets import fashion_mnist  # набор fashion MNIST
from tensorflow.python.keras.models import load_model  # работа с данными
from tensorflow.python.keras.utils.np_utils import to_categorical  # работа с данными
import numpy  # многомернымые массивы
from PIL import Image  # работа с данными

object_to_predict = numpy.random.randint(60000)


def main():
    # Загрузка набора fashion MNIST. x_train - 60000 изображений, y_train - их номера классов. x_test - 10000
    (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
    print("x_train shape:", x_train.shape, "y_train shape:", y_train.shape)

    pixels = x_train[object_to_predict]

    # Преобразование ответов из номеров классов в категориальное представление
    y_train = to_categorical(y_train, 10)
    x_train = x_train / 255

    classes = ["t-shirt", "trouser", "pullover", "dress", "coat", "sandal", "shirt", "sneaker", "bag", "ankle boot"]

    # model = load_model("fashion_model_nikita/fashion_model_base_87.h5")
    model = load_model("fashion_model_nikita_4_90.h5")

    # Создание изображения из двумерного массива путем склейки четырех двумерных массивов в один
    image = Image.fromarray(pixels, "L")

    # Распознавание элементов одежды, оценка качества обучения
    prediction = model.predict(numpy.reshape(
        x_train[object_to_predict],
        (1, 784)
    ))

    print("Object",
          classes[numpy.argmax(y_train[object_to_predict])],
          "recognised as",
          classes[numpy.argmax(prediction)],
          "with accuracy",
          numpy.max(prediction * 100),
          "percents")

    image.show()


if __name__ == "__main__":
    main()
