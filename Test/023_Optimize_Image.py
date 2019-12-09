import cv2
from matplotlib import pyplot as plt


def Image_Hist(image):
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
    plt.show()


def Equal_Hist(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dst = cv2.equalizeHist(gray)
    cv2.imshow('Equal Hist', dst)


def Clahe(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(10, 10))
    clahe = clahe.apply(gray)
    clahe = cv2.cvtColor(clahe, cv2.COLOR_GRAY2BGR)
    cv2.imshow('Clahe', clahe)


image = cv2.imread('Pictures/clouds.jpg')
cv2.imshow('Image', image)
Clahe(image)
Equal_Hist(image)

cv2.waitKey()
cv2.destroyAllWindows()
