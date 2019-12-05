import cv2
import numpy as np


def add(image, image1):
    image = cv2.add(image, image1)
    cv2.imshow("Add them", image)


def min(image, image1):
    image = cv2.min(image, image1)
    cv2.imshow("Min them", image)


def divide(image, image1):
    image = cv2.divide(image, image1)
    cv2.imshow("Divide them", image)


def multiply(image, image1):
    image = cv2.multiply(image, image1)
    cv2.imshow("Multiply them", image)


# contrast, brightness
def contrast(image, contrast, brightness):
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)

    dst = cv2.addWeighted(image, contrast, blank, 1 - contrast, brightness)

    cv2.imshow('Contrast', dst)


image = cv2.imread("Pictures/clouds.jpg")
image1 = cv2.imread("Pictures/otsu.jpg")
image = image[:200, 0:300, :]
image1 = image1[:, :, :]

# add(image, image1)
# min(image, image1)
# divide(image, image1)
# multiply(image, image1)
contrast(image, 1, 0.5)

cv2.waitKey(0)
cv2.destroyAllWindows()
