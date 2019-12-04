import cv2
from matplotlib import pyplot as plt

image = cv2.imread('Pictures/clouds.jpg', 0)
ret, threshold1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
ret, threshold2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
ret, threshold3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
ret, threshold4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
ret, threshold5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [image, threshold1, threshold2, threshold3, threshold4, threshold5]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i], fontsize=8)
    plt.xticks([]), plt.yticks([])

plt.show()
