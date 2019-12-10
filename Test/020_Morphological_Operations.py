import cv2
import numpy as np


def Open(Image, x, y):
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    cv2.imshow('Binary', binary)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (x, y))
    open = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel=kernel)
    cv2.imshow('Open' + np.str(Image), open)


def Close(Image, x, y):
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imshow('Binary', binary)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (x, y))
    close = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel=kernel)
    cv2.imshow('Close' + np.str(Image), close)


image = cv2.imread('Pictures/j_noise_out.bmp')
image1 = cv2.imread('Pictures/j_noise_in.bmp')
image2 = cv2.imread('Pictures/lines.jpg')
abcd = cv2.imread('Pictures/ABCD.jpg')
# Open(image, 5, 5)
# Close(image1, 5, 5)
Open(abcd, 8, 8)
# Open(image2, 15, 1)

cv2.waitKey()
cv2.destroyAllWindows()
