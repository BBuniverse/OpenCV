import numpy as np
import cv2

# When pressing mouse turn to true
drawing = False

# True for rectangle, False for straight line, changed by press 'm'
mode = True

ix, iy = -1, -1


def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing:
            if mode:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
            else:
                # drawing line by connective small circles
                cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        # release mouse stop drawing
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False


img = np.zeros((512, 512, 3), np.uint8)

cv2.namedWindow('Drawing')
cv2.namedWindow('Final')
cv2.setMouseCallback('Drawing', draw)

while 1:
    cv2.imshow('Drawing', img)
    k = cv2.waitKey(1) & 0xFF

    final = img.copy()
    cv2.imshow('Final', final)

    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()
