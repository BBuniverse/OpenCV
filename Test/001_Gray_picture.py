import cv2

image = cv2.imread("Pictures/clouds.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('Over the Clouds')
cv2.namedWindow('Over the Clouds - gray')
cv2.imshow('Over the Clouds', image)
cv2.imshow('Over the Clouds - gray', gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
