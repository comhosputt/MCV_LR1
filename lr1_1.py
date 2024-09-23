import cv2
import time

def normalize_minmax_opencv(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    normalized_image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

    cv2.imwrite('lr1_1.png', normalized_image)

def test_minmax_normalization():

    start_time = time.time()

    normalize_minmax_opencv('image.jpg')

    end_time = time.time()

    print(f"Время выполнения программы: {end_time - start_time} секунд")


test_minmax_normalization()
