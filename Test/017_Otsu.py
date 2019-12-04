import cv2
from matplotlib import pyplot as plt

image = cv2.imread('Pictures/otsu.jpg', 0)

ret, threshold = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
ret_otsu, otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# (5, 5) is the size of gaussian blur and 0 is standard deviation
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)
ret_otsu_blur, otsu_blur = cv2.threshold(gaussian_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

images = [image, 0, threshold,
          image, 0, otsu,
          gaussian_blur, 0, otsu_blur]
titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
          'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
          'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]

for i in range(3):
    plt.subplot(3, 3, i * 3 + 1)
    plt.imshow(images[i * 3], 'gray')
    plt.title(titles[i * 3], fontsize=8), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, i * 3 + 2)
    plt.hist(images[i * 3].ravel(), 256)
    plt.title(titles[i * 3 + 1], fontsize=8), plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, i * 3 + 3)
    plt.imshow(images[i * 3 + 2], 'gray')
    plt.title(titles[i * 3 + 2], fontsize=8), plt.xticks([]), plt.yticks([])

plt.show()
