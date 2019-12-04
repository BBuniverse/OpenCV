import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Pictures/clouds.jpg', 0)
rows, cols = img.shape

scale = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

height, width = img.shape[:2]
scale1 = cv2.resize(img, (int(width * 0.7), int(height * 0.7)), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Scale', scale)
cv2.imshow('Scale1', scale1)

matrix = np.float32([[1, 0, 100], [0, 1, 100]])
translation = cv2.warpAffine(img, matrix, (rows, cols))
cv2.imshow('Translation', translation)

#                                 rotation central, rotation degree, scale
matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 0.5)
#                                   rotation central
rotate = cv2.warpAffine(img, matrix, (cols, rows))
cv2.imshow('Rotate', rotate)

flip = cv2.flip(img, -1)
cv2.imshow('Flip', flip)

pts1 = np.float32([[56, 65], [238, 52], [28, 237], [239, 240]])
pts2 = np.float32([[0, 0], [200, 0], [0, 200], [200, 200]])
M = cv2.getPerspectiveTransform(pts1, pts2)
res = cv2.warpPerspective(img, M, (cols, rows))
plt.imshow(res)
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
