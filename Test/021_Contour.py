import cv2


def Find_Contour(Image):
    Image = cv2.GaussianBlur(Image, (3, 3), 0)
    gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    cv2.imshow('Binary Image', binary)

    contours, heriachy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for i, contour in enumerate(contours):
        cv2.drawContours(Image, contours, i, (0, 0, 255), 2)

    cv2.imshow('Contour Find', Image)


image = cv2.imread('Pictures/coins2.jpg')

Find_Contour(image)

cv2.waitKey()
cv2.destroyAllWindows()
