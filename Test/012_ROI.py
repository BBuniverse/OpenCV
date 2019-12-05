import cv2
import numpy as np


def fill_color(image):
    copyimage = image.copy()
    height, weight = image.shape[:2]
    mask = np.zeros([height + 2, weight + 2], np.uint8)
    cv2.floodFill(copyimage, mask, (300, 300), (0, 255, 0), (100, 100, 100), (50, 50, 50), cv2.FLOODFILL_FIXED_RANGE)
    cv2.imshow('Filled', copyimage)


image = cv2.imread('Pictures/clouds.jpg')

selected = image[50:200, 50:200]
image[100:250, 100:250] = selected

cv2.namedWindow('Image')
cv2.imshow('Image', image)
print(image.shape)
fill_color(image)

cv2.waitKey()
cv2.destroyAllWindows()
