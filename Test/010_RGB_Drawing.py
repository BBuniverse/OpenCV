import cv2
import numpy as np


def nothing(x):
    pass


# When pressing mouse turn to true
drawing = False

# True for rectangle, False for straight line, changed by pressing 'm'
mode = True

start = end = (0, 0)
colors = (0, 0, 255)


def draw(event, x, y, flags, param):
    global start, end, drawing, mode, colors

    r = cv2.getTrackbarPos('R', 'Drawing')
    g = cv2.getTrackbarPos('G', 'Drawing')
    b = cv2.getTrackbarPos('B', 'Drawing')
    color = (b, g, r)
    colors = color

    # Color notify
    cv2.circle(image, (480, 20), 20, color, -1)
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                end = (x, y)
            else:
                # drawing line by connective small circles
                cv2.circle(image, (x, y), 3, color, -1)
        # release mouse stop drawing
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(image, start, end, colors, 2)
        start = end = (0, 0)


image = np.zeros((512, 512, 3), np.uint8)

cv2.namedWindow('Drawing')
cv2.createTrackbar('R', 'Drawing', 0, 255, nothing)
cv2.createTrackbar('G', 'Drawing', 0, 255, nothing)
cv2.createTrackbar('B', 'Drawing', 0, 255, nothing)

cv2.setMouseCallback('Drawing', draw)

while 1:
    k = cv2.waitKey(1) & 0xFF

    final = np.copy(image)
    if drawing and end != (0, 0) and mode:
        cv2.rectangle(final, start, end, colors, 2)
    cv2.imshow('Drawing', final)

    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()
