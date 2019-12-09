import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('Pictures/gaussian_noise.bmp')

plt.subplot(131)
plt.imshow(image), plt.title('Original', fontsize=8)
plt.xticks([]), plt.yticks([])

kernel = np.ones((5, 5), np.float32) / 25
# kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]], np.float32)
dst = cv2.filter2D(image, -1, kernel=kernel)
plt.subplot(132)
plt.imshow(dst), plt.title('Averaging', fontsize=8)
plt.xticks([]), plt.yticks([])

gaussian = cv2.GaussianBlur(image, (5, 5), 0)
plt.subplot(133)
plt.imshow(gaussian), plt.title('Gaussian', fontsize=8)
plt.xticks([]), plt.yticks([])
plt.show()

# Compare Blur with Median
image = cv2.imread('Pictures/salt_noise.bmp')

plt.subplot(131)
plt.imshow(image), plt.title('Original', fontsize=8)
plt.xticks([]), plt.yticks([])

# Remove the noise
blur = cv2.blur(image, (5, 5))
plt.subplot(132)
plt.imshow(blur), plt.title('Blurred', fontsize=8)
plt.xticks([]), plt.yticks([])

# Remove High contrast noise
median = cv2.medianBlur(image, 5)
plt.subplot(133)
plt.imshow(median), plt.title('Median', fontsize=8)
plt.xticks([]), plt.yticks([])
plt.show()

# Compare Gaussian with Bilateral
image = cv2.imread('Pictures/otsu.jpg')

plt.subplot(131)
plt.imshow(image), plt.title('Original', fontsize=8)
plt.xticks([]), plt.yticks([])

gaussian = cv2.GaussianBlur(image, (5, 5), 0)
plt.subplot(132)
plt.imshow(gaussian), plt.title('Gaussian', fontsize=8)
plt.xticks([]), plt.yticks([])

#                                    distance
bilateral = cv2.bilateralFilter(image, 0, 100, 15)
plt.subplot(133)
plt.imshow(bilateral), plt.title('Bilateral', fontsize=8)
plt.xticks([]), plt.yticks([])
plt.show()
