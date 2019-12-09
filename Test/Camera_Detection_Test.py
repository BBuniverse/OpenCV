import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow('Video')


def CalcBack(target, sample):
    target_hsv = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)
    sample_hsv = cv2.cvtColor(sample, cv2.COLOR_BGR2HSV)

    sample_hist = cv2.calcHist([sample_hsv], [0, 1], None, [32, 48], [0, 180, 0, 256])

    cv2.normalize(sample_hist, sample_hist, 0, 255, cv2.NORM_MINMAX)
    calcBack = cv2.calcBackProject([target_hsv], [0, 1], sample_hist, [0, 180, 0, 256], 1)
    cv2.imshow('CalcBack', calcBack)
    cv2.imshow('Sample', sample)


while True:
    ret, video = cap.read()
    # video = video[:, :, 2]
    # video = cv2.flip(video, 1)
    # ret, threshold = cv2.threshold(video, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    #
    # contours, hierachy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # color = cv2.cvtColor(video, cv2.COLOR_GRAY2BGR)
    # cv2.drawContours(color, contours, -1, (0, 0, 255), 2)
    #
    # for i in range(len(contours)):
    #     minrect = cv2.minAreaRect(contours[i])
    #     box = np.int0(cv2.boxPoints(minrect))
    #     cv2.drawContours(color, [box], 0, (255, 0, 0), 2)
    #
    # cv2.imshow('Video', color)
    sample = video[50:100, 50:100]
    CalcBack(video, sample)
    cv2.imshow('x', video)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
