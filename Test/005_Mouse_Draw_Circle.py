import numpy as np
import cv2


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (2550, 0, 0), 10)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Double click Drawing Circle')
cv2.setMouseCallback('Double click Drawing Circle', draw_circle)

while 1:
    cv2.imshow('Double click Drawing Circle', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
