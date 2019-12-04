import cv2

img = cv2.imread('clouds.jpg')

x = img[50:200, 50:200]
img[100:250, 100:250] = x

cv2.imshow('frame', img)
cv2.waitKey()
cv2.destroyAllWindows()
