import cv2
import numpy as np
from matplotlib import pyplot as plt


def Hough_Line(Image):
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(canny, 1, np.pi / 180, 200)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        cv2.line(Image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imshow("Hough Line", Image)


def Possible_Line(Image):
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLinesP(canny, 1, np.pi / 180, 100, minLineLength=150, maxLineGap=10)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(Image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imshow("Possible Line", Image)


def Hough_Circle(Image):
    dst = cv2.pyrMeanShiftFiltering(Image, 10, 100)
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=80, param2=30, minRadius=0, maxRadius=0)

    for circle in circles[0]:
        cv2.circle(Image, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)
        cv2.circle(Image, (circle[0], circle[1]), 2, (0, 0, 255), 2)

    cv2.imshow('Hough Circle', Image)


image = cv2.imread('Pictures/line.jpg')
image1 = cv2.imread('Pictures/coins.jpg')

Possible_Line(image)
# Hough_Circle(image1)

plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
