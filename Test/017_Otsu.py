import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Pictures/otsu.jpg', 0)

ret, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
retotsu, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# (5, 5) is the size of gaussian blur and 0 is standard deviation
gaussianblur = cv2.GaussianBlur(img, (5, 5), 0)
retotsublur, otsublur = cv2.threshold(gaussianblur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

images = [img, 0, threshold,
          img, 0, otsu,
          gaussianblur, 0, otsublur]
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
