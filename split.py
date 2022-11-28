import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('park',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

b,g,r = cv.split(img)

cv.imshow('Blue',b)
cv.imshow('green',g)
cv.imshow('reg',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merged',merged)

blue = cv.merge([b,blank,blank])
cv.imshow('bl',blue)

red = cv.merge([blank,blank,r])
cv.imshow('re',red)

green = cv.merge([blank,g,blank])
cv.imshow('gr',green)

cv.waitKey(0)