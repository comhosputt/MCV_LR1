import cv2
import time

# Функция для нормирования изображения с использованием MinMax через OpenCV
def normalize_minmax_opencv(image_path):
    # Загрузка изображения
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Нормирование MinMax с использованием встроенной функции
    normalized_image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

    # Сохранение результата
    cv2.imwrite('lr1_1.png', normalized_image)

# Функция для измерения времени выполнения
def test_minmax_normalization():

    # Запускаем таймер
    start_time = time.time()

    # Пример использования
    normalize_minmax_opencv('image.jpg')

    # Останавливаем таймер
    end_time = time.time()

    # Выводим время выполнения
    print(f"Время выполнения программы: {end_time - start_time} секунд")


test_minmax_normalization()