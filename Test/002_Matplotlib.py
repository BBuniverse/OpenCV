import cv2
import numpy as np

from matplotlib import pyplot as plt

print("OpenCV version:")
print(cv2.__version__)

img = cv2.imread("clouds.jpg", 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])

plt.show()
