import cv2
import numpy as np

image = cv2.imread('Pictures/clothes.jpg', 0)


def nothing():
    pass


cv2.namedWindow('Edge')
cv2.createTrackbar('Max', 'Edge', 90, 255, nothing)
cv2.createTrackbar('Min', 'Edge', 40, 255, nothing)

while True:
    # max / min should between 2:1 to 3:1
    max_value = cv2.getTrackbarPos('Max', 'Edge')
    min_value = cv2.getTrackbarPos('Min', 'Edge')

    gaussian = cv2.GaussianBlur(image, (5, 5), 1)
    edges = cv2.Canny(gaussian, min_value, max_value)
    cv2.imshow('Edge', np.hstack((image, edges)))

    if cv2.waitKey(1) == 27:
        break

cv2.waitKey()
cv2.destroyAllWindows()
