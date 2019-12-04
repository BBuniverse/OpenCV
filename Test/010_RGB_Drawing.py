import numpy as np
import cv2


def nothing(x):
    pass


# When pressing mouse turn to true
drawing = False

# True for rectangle, False for straight line, changed by pressing 'm'
mode = True

ix, iy = -1, -1


def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode

    r = cv2.getTrackbarPos('R', 'Drawing')
    g = cv2.getTrackbarPos('G', 'Drawing')
    b = cv2.getTrackbarPos('B', 'Drawing')
    color = (b, g, r)

    # Color notify
    cv2.circle(img, (480, 20), 20, color, -1)
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing:
            if mode:
                cv2.rectangle(img, (ix, iy), (x, y), color, 2)
            else:
                # drawing line by connective small circles
                cv2.circle(img, (x, y), 3, color, -1)
        # release mouse stop drawing
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False


img = np.zeros((512, 512, 3), np.uint8)

cv2.namedWindow('Drawing')
cv2.createTrackbar('R', 'Drawing', 0, 255, nothing)
cv2.createTrackbar('G', 'Drawing', 0, 255, nothing)
cv2.createTrackbar('B', 'Drawing', 0, 255, nothing)

cv2.namedWindow('Final')
cv2.setMouseCallback('Drawing', draw)

while 1:
    k = cv2.waitKey(1) & 0xFF

    final = img.copy()
    cv2.imshow('Final', final)
    cv2.imshow('Drawing', img)

    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()
