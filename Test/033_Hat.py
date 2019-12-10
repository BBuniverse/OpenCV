import cv2


# Colored picture
def Top_Hat(Image):
    cv2.imshow('Original', Image)
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dst = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel=kernel)
    cv2.imshow('Top Hat', dst)


def Black_Hat(Image):
    cv2.imshow('Original', Image)
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dst = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel=kernel)
    cv2.imshow('Black Hat', dst)


def Gradient(Image):
    cv2.imshow('Original', Image)
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dst = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel=kernel)
    cv2.imshow('Gradient', dst)


image = cv2.imread('Pictures/clothes.jpg')
Gradient(image)
cv2.waitKey()
cv2.destroyAllWindows()
