import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Pictures/gaussian_noise.bmp')

plt.subplot(131)
plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])

kernel = np.ones((5, 5), np.float32) / 25

dst = cv2.filter2D(img, -1, kernel)
plt.subplot(132)
plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])

gaussian = cv2.GaussianBlur(img, (5, 5), 0)
plt.subplot(133)
plt.imshow(gaussian), plt.title('Gaussian')
plt.xticks([]), plt.yticks([])
plt.show()

# Compare Blur with Median
img = cv2.imread('Pictures/salt_noise.bmp')

plt.subplot(131)
plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])

blur = cv2.blur(img, (5, 5))
plt.subplot(132)
plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])

median = cv2.medianBlur(img, 5)
plt.subplot(133)
plt.imshow(median), plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.show()

# Compare Gaussian with Bilateral
img = cv2.imread('Pictures/otsu.jpg')

plt.subplot(131)
plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])

gaussian = cv2.GaussianBlur(img, (5, 5), 0)
plt.subplot(132)
plt.imshow(gaussian), plt.title('Gaussian')
plt.xticks([]), plt.yticks([])

bilateral = cv2.bilateralFilter(img, 9, 75, 75)
plt.subplot(133)
plt.imshow(bilateral), plt.title('Bilateral')
plt.xticks([]), plt.yticks([])
plt.show()
