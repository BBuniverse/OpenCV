import cv2

capture = cv2.VideoCapture(0)

cv2.namedWindow('Video')

while True:
    ret, video = capture.read()

    cv2.imshow('Video', video)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
