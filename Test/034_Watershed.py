import cv2
import numpy as np
from matplotlib import pyplot as plt


def Watershed(Image):
    blurred = cv2.pyrMeanShiftFiltering(Image, 10, 100)

    # Gray
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # cv2.imshow('Binary', binary)

    # Morphological
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    open = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel=kernel, iterations=2)
    sure_bg = cv2.dilate(open, kernel=kernel, iterations=2)
    cv2.imshow('Sure_bg', sure_bg)

    # Distance
    distance = cv2.distanceTransform(open, 1, 5)
    distance = cv2.normalize(distance, 0, 1.0, cv2.NORM_MINMAX)
    # cv2.imshow('Distance', distance * 50)

    ret, sure_fg = cv2.threshold(distance, distance.max() * 0.5, 255, 0)
    cv2.imshow('Sure_fg', sure_fg)

    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    ret, markers = cv2.connectedComponents(sure_fg)

    # watershed transform
    markers = markers + 1
    markers[unknown == 255] = 0
    markers = cv2.watershed(Image, markers=markers)
    Image[markers == -1] = [0, 0, 255]
    cv2.imshow('Result', Image)


image = cv2.imread('Pictures/coins2.jpg')
Watershed(image)

plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
