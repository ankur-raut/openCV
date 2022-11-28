import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('park',img)

#greyScale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey',grey)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

# #BGR to LAB
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('lab',lab)

# #BGR to RGB
# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('rgb',rgb)

# img = cv.imread('Resources/Photos/gray.jpg')
# cv.imshow('gray',img)

# plt.imshow(rgb)
# plt.show()

#BGR to RGB
gry_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('gry_bgr',gry_bgr)

cv.waitKey(0)