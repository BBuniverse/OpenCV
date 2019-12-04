import cv2
import numpy as np

img = cv2.imread('Pictures/handwriting.jpg', 0)
ret, threshold = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

gray = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

cv2.drawContours(gray, contours, -1, (0, 0, 255), 2)

# Rectangle
x, y, w, h = cv2.boundingRect(contours[0])
cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Minimal Rectangle
minrect = cv2.minAreaRect(contours[0])
box = np.int0(cv2.boxPoints(minrect))
cv2.drawContours(gray, [box], 0, (255, 0, 0), 2)

# Circle
(x, y), radius = cv2.minEnclosingCircle(contours[1])
(x, y, radius) = np.int0((x, y, radius))
cv2.circle(gray, (x, y), radius, (200, 100, 50), 2)

# Ellipse
ellipse = cv2.fitEllipse(contours[1])
cv2.ellipse(gray, ellipse, (150, 0, 150), 2)

cv2.namedWindow('Contour')
cv2.imshow('Contour', gray)

cv2.waitKey()
cv2.destroyAllWindows()
