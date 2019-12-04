import cv2
import numpy as np

capture = cv2.VideoCapture('/Users/bowen/Documents/Video/MV/MV_.mp4')

while (capture.isOpened()):
    ret, frame = capture.read()

    cv2.imshow('frame', frame)

    # The larger number the speed of playing slower
    if cv2.waitKey(1) == ord('q'):
        break
