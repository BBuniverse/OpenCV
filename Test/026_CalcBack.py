import cv2
from matplotlib import pyplot as plt

target = cv2.imread('Pictures/clouds.jpg')
sample = target[114:128, 409:438]


def CalcBack(target, sample):
    target_hsv = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)
    sample_hsv = cv2.cvtColor(sample, cv2.COLOR_BGR2HSV)

    sample_hist = cv2.calcHist([sample_hsv], [0, 1], None, [32, 48], [0, 180, 0, 256])
    plt.imshow(sample_hist, interpolation='nearest')
    plt.title('Hist')
    plt.show()

    cv2.normalize(sample_hist, sample_hist, 0, 255, cv2.NORM_MINMAX)
    calcBack = cv2.calcBackProject([target_hsv], [0, 1], sample_hist, [0, 180, 0, 256], 1)

    dis = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dst = cv2.filter2D(calcBack, -1, dis)

    cv2.imshow('Origin', target)
    cv2.imshow('Sample', sample)
    cv2.imshow('CalcBack', calcBack)
    cv2.imshow('Element', dst)


CalcBack(target, sample)
cv2.waitKey()
cv2.destroyAllWindows()
