import cv2
import os

capture = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
os.remove('Pictures/004_Camera_Recording.avi')
outfile = cv2.VideoWriter('Pictures/004_Camera_Recording.avi', fourcc, 25., (400, 705))
print('Start recording')

while (capture.isOpened()):
    ret, frame = capture.read()

    if ret:
        outfile.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

print('Recording finished')
cv2.destroyAllWindows()
