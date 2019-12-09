import cv2
import numpy as np


def Sobel(Image):
    grad_x = cv2.Sobel(Image, cv2.CV_32F, 1, 0)
    grad_y = cv2.Sobel(Image, cv2.CV_32F, 0, 1)

    gradx = cv2.convertScaleAbs(grad_x)
    grady = cv2.convertScaleAbs(grad_y)

    cv2.imshow('Gradex', gradx)
    cv2.imshow('Gradey', grady)

    gradxy = cv2.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv2.imshow('Gradexy', gradxy)


def Lpls(Image):
    dst = cv2.Laplacian(Image, cv2.CV_32F)

    # # kernel4 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    # kernel8 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    # dst = cv2.filter2D(Image, cv2.CV_32F, kernel=kernel8)
    lpls = cv2.convertScaleAbs(dst)
    cv2.imshow('Lpls', lpls)


image = cv2.imread('Pictures/sudoku.jpg')
cv2.imshow('Original', image)
Sobel(image)
Lpls(image)

cv2.waitKey()
cv2.destroyAllWindows()
