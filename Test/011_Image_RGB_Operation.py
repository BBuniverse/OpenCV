import cv2

image = cv2.imread('Pictures/clouds.jpg')

b, g, r = cv2.split(image)

cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)

merge = cv2.merge((g, b, r))

cv2.namedWindow('Merge GBR')
cv2.imshow('Merge GBR', merge)

cv2.waitKey()
cv2.destroyAllWindows()
