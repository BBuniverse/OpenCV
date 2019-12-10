import cv2
import numpy as np


def Measure_Object(Image):
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imshow('Binary Image', binary)
    contours, hireachy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    dst = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        mm = cv2.moments(contour)
        if mm['m00'] > 0:
            cx = mm['m10'] / mm['m00']
            cy = mm['m01'] / mm['m00']
            cv2.circle(Image, (np.int(cx), np.int(cy)), 2, (0, 255, 200), -1)
            cv2.rectangle(Image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            approxPoly = cv2.approxPolyDP(contour, 4, True)
            if approxPoly.shape[0] > 6:
                cv2.drawContours(dst, contours, i, (0, 0, 255), 2)
            if approxPoly.shape[0] == 4:
                cv2.drawContours(dst, contours, i, (0, 255, 0), 2)

    cv2.imshow('Measure Object', Image)
    cv2.imshow('Distinguish Circle and rectangle', dst)


image = cv2.imread('Pictures/circle rectangle.jpg')
Measure_Object(image)

cv2.waitKey()
cv2.destroyAllWindows()
