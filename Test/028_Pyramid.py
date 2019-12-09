import cv2
import numpy as np


def Pyramid_Down(Image):
    level = 3
    temp = Image.copy()
    pyramid_images = []
    for i in range(level):
        pyr = cv2.pyrDown(temp)
        pyramid_images.append(pyr)
        temp = pyr.copy()
        cv2.imshow('Pyramid Down' + np.str(i), pyr)
        print(pyr.shape)
    return pyramid_images


def Pyramid_Up(Image):
    pyramid_images = Pyramid_Down(Image)
    level = len(pyramid_images)
    for i in range(level - 1, -1, -1):
        if (i - 1) < 0:
            expand = cv2.pyrUp(pyramid_images[i], dstsize=Image.shape[:2])
            lpls = cv2.subtract(Image, expand)
            cv2.imshow('Lpls' + np.str(i), lpls)
        else:
            expand = cv2.pyrUp(pyramid_images[i], dstsize=pyramid_images[i - 1].shape[:2])
            lpls = cv2.subtract(pyramid_images[i - 1], expand)
            cv2.imshow('Lpls' + np.str(i), lpls)


image = cv2.imread('Pictures/lena.jpg')

Pyramid_Up(image)
cv2.waitKey()
cv2.destroyAllWindows()
