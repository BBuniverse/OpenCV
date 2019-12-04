import cv2

image = cv2.imread('Pictures/clouds.jpg')

selected = image[50:200, 50:200]
image[100:250, 100:250] = selected

cv2.namedWindow('Image')
cv2.imshow('Image', image)

cv2.waitKey()
cv2.destroyAllWindows()
