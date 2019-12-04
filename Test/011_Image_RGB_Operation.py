import cv2

img = cv2.imread('Pictures/clouds.jpg')

b, g, r = cv2.split(img)

cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)

x = cv2.merge((g, b, r))
cv2.imshow('merge', x)

cv2.waitKey()
cv2.destroyAllWindows()
