import os
import cv2

capture = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
os.remove('Pictures/004_Camera_Recording.avi')
outfile = cv2.VideoWriter('Pictures/004_Camera_Recording.avi', fourcc, 25., (400, 705))
print('Start recording')

cv2.namedWindow('Video')

while (capture.isOpened()):
    ret, video = capture.read()

    if ret:
        outfile.write(video)

        cv2.imshow('Video', video)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

print('Recording finished')
cv2.destroyAllWindows()
