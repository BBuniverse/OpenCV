import cv2
from matplotlib import pyplot as plt

image = cv2.imread("Pictures/clouds.jpg")
plt.imshow(image)
plt.xticks([]), plt.yticks([])

plt.show()
