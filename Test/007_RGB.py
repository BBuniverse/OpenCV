import numpy as np
import cv2


def nothing(x):
    pass


img = np.zeros((300, 500, 3), np.uint8)
cv2.namedWindow('Image')

cv2.createTrackbar('R', 'Image', 0, 255, nothing)
cv2.createTrackbar('G', 'Image', 0, 255, nothing)
cv2.createTrackbar('B', 'Image', 0, 255, nothing)

switch = '0:0FF\n:ON'
cv2.createTrackbar(switch, 'Image', 0, 1, nothing)

while 1:
    cv2.imshow('Image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    r = cv2.getTrackbarPos('R', 'Image')
    g = cv2.getTrackbarPos('G', 'Image')
    b = cv2.getTrackbarPos('B', 'Image')
    s = cv2.getTrackbarPos(switch, 'Image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [r, g, b]

cv2.destroyAllWindows()
