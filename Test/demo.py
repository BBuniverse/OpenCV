import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('Pictures/hist.jpg')
img = img[:, :, 2]
equ = cv2.equalizeHist(img)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)

plt.subplot(231)
plt.imshow(img), plt.title('Origin', fontsize=8)
plt.xticks([]), plt.yticks([])

hist = np.bincount(img.ravel(), minlength=256)
plt.subplot(234)
plt.plot(hist)
plt.xticks([]), plt.yticks([])

plt.subplot(232)
plt.imshow(equ), plt.title('Equ', fontsize=8)
plt.xticks([]), plt.yticks([])

hist = np.bincount(equ.ravel(), minlength=256)
plt.subplot(235)
plt.plot(hist)
plt.xticks([]), plt.yticks([])

plt.subplot(233)
plt.imshow(cl1), plt.title('Clane', fontsize=8)
plt.xticks([]), plt.yticks([])

hist = np.bincount(cl1.ravel(), minlength=256)
plt.subplot(236)
plt.plot(hist)
plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
