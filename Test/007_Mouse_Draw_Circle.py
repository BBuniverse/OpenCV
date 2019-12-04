import cv2
import numpy as np


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image, (x, y), 100, (2550, 0, 0), 10)


image = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Double click to Draw a Circle')
cv2.setMouseCallback('Double click to Draw a Circle', draw_circle)

while 1:
    cv2.imshow('Double click to Draw a Circle', image)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
