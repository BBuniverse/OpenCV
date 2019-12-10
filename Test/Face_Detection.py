# -*- coding: UTF-8 -*-
import cv2


def Face_Detect(Image):
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier(
        '/Users/bowen/PycharmProjects/OpenCV/Test/Package/haarcascade_frontalface_alt2.xml')
    faces = face_detector.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in faces:
        cv2.rectangle(Image, (x, y), (x + w, y + h), (0, 0, 255), 4)


capture = cv2.VideoCapture(0)
while True:
    ret, video = capture.read()
    video = cv2.flip(video, 1)
    Face_Detect(video)
    cv2.imshow('x', video)

    c = cv2.waitKey(10)
    if c == 27:
        break

capture.release()
cv2.destroyAllWindows()
