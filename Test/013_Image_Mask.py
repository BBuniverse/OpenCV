import cv2
import numpy as np

capture = cv2.VideoCapture(0)

lower_blue = np.array([100, 110, 110])
upper_blue = np.array([130, 255, 255])

cv2.namedWindow('Video')
cv2.namedWindow('Mask')
cv2.namedWindow('Detected')

while 1:
    ret, video = capture.read()

    hsv = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    detected = cv2.bitwise_and(video, video, mask=mask)

    cv2.imshow('Video', video)
    cv2.imshow('Mask', mask)
    cv2.imshow('Detected', detected)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
