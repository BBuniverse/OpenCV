import cv2
import numpy as np

image = cv2.imread('Pictures/j.bmp', 0)

kernel = np.ones((5, 5), np.uint8)

# Erosion and Dilation
erosion = cv2.erode(image, kernel, iterations=1)
dilation = cv2.dilate(image, kernel, iterations=1)

cv2.namedWindow('Erosion and Dilation')
cv2.imshow('Erosion and Dilation', np.hstack((image, erosion, dilation)))

# Open and Close
open = cv2.imread('Pictures/j_noise_out.bmp', 0)
opening = cv2.morphologyEx(open, cv2.MORPH_OPEN, kernel)

close = cv2.imread('Pictures/j_noise_in.bmp', 0)
closing = cv2.morphologyEx(close, cv2.MORPH_CLOSE, kernel)

cv2.namedWindow('Open and Close')
cv2.imshow('Open and Close', np.hstack((open, opening, close, closing)))

# dilation - erosion
image = cv2.imread('Pictures/clothes.jpg', 0)
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

cv2.namedWindow('Gradient')
cv2.imshow('Gradient', np.hstack((image, gradient)))

cv2.waitKey()
cv2.destroyAllWindows()
