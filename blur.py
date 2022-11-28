import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('cat',img)

#averaging
average = cv.blur(img,(7,7))
cv.imshow('avg',average)

#gauss
gaus = cv.GaussianBlur(img,(7,7),0)
cv.imshow('gaus',gaus)

#median
med = cv.medianBlur(img,7)
cv.imshow('med',med)

#bilateral
bilat = cv.bilateralFilter(img,5,15,15)
cv.imshow('bilat',bilat)

cv.waitKey(0)