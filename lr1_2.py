import numpy as np
import time
from PIL import Image


def minmax_normalization_native(image_array):
    min_val = np.min(image_array)
    max_val = np.max(image_array)
    height, width = image_array.shape

    # Массив для нормализованного изображения
    normalized_image_array = np.zeros_like(image_array, dtype=np.float32)


    for i in range(height):
        for j in range(width):
            if max_val != min_val:
                # Используем float для вычислений
                normalized_image_array[i, j] = (255.0 * (image_array[i, j] - min_val) / (max_val - min_val))
            else:
                normalized_image_array[i, j] = 0.0  # Если все значения одинаковые

    # Преобразование обратно в uint8
    normalized_image_array = np.clip(normalized_image_array, 0, 255).astype(np.uint8)

    return normalized_image_array


def test_minmax_normalization():
    image = Image.open('image.jpg').convert('L')  
    image_array = np.array(image)

    start_time = time.time()

    normalized_image = minmax_normalization_native(image_array)

    end_time = time.time()

    normalized_image_pil = Image.fromarray(normalized_image)
    normalized_image_pil.save('lr1_2.jpg')

    print(f"Время выполнения программы: {end_time - start_time} секунд")


test_minmax_normalization()
