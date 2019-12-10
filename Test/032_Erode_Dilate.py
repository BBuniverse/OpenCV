import cv2


def Erode(Image):
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    cv2.imshow('Binary', binary)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    erode = cv2.erode(binary, kernel)
    cv2.imshow('Erode', erode)


def Dilate(Image):
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    cv2.imshow('Binary', binary)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    dilate = cv2.dilate(binary, kernel)
    cv2.imshow('Dilate', dilate)


image = cv2.imread('Pictures/handwriting.jpg')
Erode(image)
Dilate(image)

cv2.waitKey()
cv2.destroyAllWindows()
