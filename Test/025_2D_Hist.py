import cv2
from matplotlib import pyplot as plt


def Hist_2D(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    plt.imshow(hist, interpolation='nearest')


image = cv2.imread('Pictures/clouds.jpg')
Hist_2D(image)

plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
