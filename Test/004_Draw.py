import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 10)

cv2.rectangle(img, (384, 0), (510, 128), (0, 200, 0), 2)

cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (20, 400), font, 4, (255, 255, 255), 10)

cv2.imshow("line", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
