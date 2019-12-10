import cv2


def OCR(Image):
    cv2.imshow('Original', Image)
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 3))
    bin1 = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel=kernel)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 1))
    bin1 = cv2.morphologyEx(bin1, cv2.MORPH_OPEN, kernel=kernel)
    cv2.imshow('Binary', bin1)


image = cv2.imread('Pictures/yzm2.jpg')

OCR(image)

cv2.waitKey()
cv2.destroyAllWindows()
