import cv2

img = cv2.imread('Pictures/handwriting.jpg')
img = img[:, :, 2]

ret, threshold = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

gray = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

cv2.drawContours(gray, contours, -1, (0, 0, 255), 2)

cv2.imshow('Contour', gray)

cv2.waitKey()
cv2.destroyAllWindows()
