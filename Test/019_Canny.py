import cv2
import numpy as np

image = cv2.imread('Pictures/sudoku.jpg')


def nothing():
    pass


def Edge(Image):
    cv2.namedWindow('Canny')
    cv2.createTrackbar('Max', 'Canny', 90, 255, nothing)
    cv2.createTrackbar('Min', 'Canny', 40, 255, nothing)
    while True:
        blurred = cv2.GaussianBlur(Image, (3, 3), 0)
        gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
        grad_x = cv2.Sobel(gray, cv2.CV_16SC1, 1, 0)
        grad_y = cv2.Sobel(gray, cv2.CV_16SC1, 0, 1)

        max_value = cv2.getTrackbarPos('Max', 'Canny')
        min_value = cv2.getTrackbarPos('Min', 'Canny')

        canny = cv2.Canny(grad_x, grad_y, min_value, max_value)
        canny_colored = cv2.bitwise_and(Image, Image, mask=canny)
        cv2.imshow('Canny', np.hstack((Image, canny_colored)))
        if cv2.waitKey(1) == 27:
            break


Edge(image)

cv2.waitKey()
cv2.destroyAllWindows()
