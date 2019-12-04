import numpy as np
import cv2

img = cv2.imread('Pictures/clothes.jpg', 0)


def track_back():
    pass


cv2.namedWindow('Edge')
cv2.createTrackbar('Max', 'Edge', 90, 255, track_back)
cv2.createTrackbar('Min', 'Edge', 40, 255, track_back)

while True:
    # max / min should between 2:1 to 3:1
    max_value = cv2.getTrackbarPos('Max', 'Edge')
    min_value = cv2.getTrackbarPos('Min', 'Edge')

    gaussian = cv2.GaussianBlur(img, (5, 5), 1)
    edges = cv2.Canny(gaussian, min_value, max_value)
    cv2.imshow('Edge', np.hstack((img, edges)))

    if cv2.waitKey(1) == 27:
        break

cv2.waitKey()
cv2.destroyAllWindows()
