import numpy as np
import time
from PIL import Image


# Функция для нативного нормирования MinMax
def minmax_normalization_native(image_array):
    min_val = np.min(image_array)
    max_val = np.max(image_array)
    height, width = image_array.shape

    # Создаем массив для нормализованного изображения
    normalized_image_array = np.zeros_like(image_array, dtype=np.float32)

    # Нормируем каждый пиксель вручную
    for i in range(height):
        for j in range(width):
            if max_val != min_val:
                # Используем float для вычислений
                normalized_image_array[i, j] = (255.0 * (image_array[i, j] - min_val) / (max_val - min_val))
            else:
                normalized_image_array[i, j] = 0.0  # Если все значения одинаковые

    # Преобразуем обратно в uint8, используя clip
    normalized_image_array = np.clip(normalized_image_array, 0, 255).astype(np.uint8)

    return normalized_image_array


# Тестовая функция для измерения времени выполнения
def test_minmax_normalization():
    # Загрузка изображения
    image = Image.open('image.jpg').convert('L')  # Преобразуем в градации серого
    image_array = np.array(image)

    # Запускаем таймер
    start_time = time.time()

    # Применяем нормирование MinMax
    normalized_image = minmax_normalization_native(image_array)

    # Останавливаем таймер
    end_time = time.time()

    # Сохраняем нормализованное изображение
    normalized_image_pil = Image.fromarray(normalized_image)
    normalized_image_pil.save('lr1_2.jpg')

    # Выводим время выполнения
    print(f"Время выполнения программы: {end_time - start_time} секунд")


# Запуск теста
test_minmax_normalization()