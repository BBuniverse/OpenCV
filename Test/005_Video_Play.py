import cv2

capture = cv2.VideoCapture('/Users/bowen/Documents/Video/MV/MV_.mp4')

cv2.namedWindow('Video')

while (capture.isOpened()):
    ret, video = capture.read()

    cv2.imshow('Video', video)

    # The larger number the speed of playing slower
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
