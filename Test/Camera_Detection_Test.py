import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = frame[:, :, 2]
    frame = cv2.flip(frame, 1)
    ret, threshold = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    contours, hierachy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    gray = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(gray, contours, -1, (0, 0, 255), 2)

    for i in range(len(contours)):
        minrect = cv2.minAreaRect(contours[i])
        box = np.int0(cv2.boxPoints(minrect))
        cv2.drawContours(gray, [box], 0, (255, 0, 0), 2)

    cv2.imshow('frame', gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
