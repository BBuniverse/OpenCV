import numpy as np
import cv2

img = cv2.imread('Pictures/j.bmp', 0)

kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('Erosion and Dilation', np.hstack((img, erosion, dilation)))

open = cv2.imread('Pictures/j_noise_out.bmp', 0)
opening = cv2.morphologyEx(open, cv2.MORPH_OPEN, kernel)

close = cv2.imread('Pictures/j_noise_in.bmp', 0)
closing = cv2.morphologyEx(close, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Open and Close', np.hstack((open, opening, close, closing)))

# dilation - erosion
img = cv2.imread('Pictures/clothes.jpg', 0)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('Gradient', np.hstack((img, gradient)))

cv2.waitKey()
cv2.destroyAllWindows()
