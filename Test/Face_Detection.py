# -*- coding: UTF-8 -*-
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(
    '/Users/bowen/PycharmProjects/OpenCV/Test/Package/haarcascade_frontalface_alt2.xml')

while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5))
    for (x, y, w, h) in faces:
        cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)

    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    cv2.imshow('Face Recognition', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
