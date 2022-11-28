import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#simple thresholding
threshold,thresh = cv.threshold(gray,100,256,cv.THRESH_BINARY)
cv.imshow('simpleThresh',thresh)

threshold,thresh_inv = cv.threshold(gray,100,256,cv.THRESH_BINARY_INV)
cv.imshow('simpleThresh_inv',thresh_inv)

#adaptive thresh
adaptive = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('adaptive',adaptive)


cv.waitKey(0)