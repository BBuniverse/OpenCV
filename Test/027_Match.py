import cv2
import numpy as np


def Pattern_Match():
    image = cv2.imread('Pictures/mario.jpg')
    pattern = cv2.imread('Pictures/mario_coin.jpg')
    cv2.imshow('Image', image)
    cv2.imshow('Pattern', pattern)

    methods = [cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_CCOEFF_NORMED]
    height, weight = pattern.shape[:2]
    for method in methods:
        result = cv2.matchTemplate(image, pattern, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if method == cv2.TM_SQDIFF_NORMED:
            top_left = min_loc
        else:
            top_left = max_loc

        bottom_right = (top_left[0] + weight, top_left[1] + height)
        cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 1)
        cv2.imshow("Image Match" + np.str(method), image)


Pattern_Match()
cv2.waitKey()
cv2.destroyAllWindows()
