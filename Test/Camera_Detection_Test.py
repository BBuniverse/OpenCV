import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow('Video')

while True:
    ret, video = cap.read()
    video = video[:, :, 2]
    video = cv2.flip(video, 1)
    ret, threshold = cv2.threshold(video, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    contours, hierachy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    color = cv2.cvtColor(video, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(color, contours, -1, (0, 0, 255), 2)

    for i in range(len(contours)):
        minrect = cv2.minAreaRect(contours[i])
        box = np.int0(cv2.boxPoints(minrect))
        cv2.drawContours(color, [box], 0, (255, 0, 0), 2)

    cv2.imshow('Video', color)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
