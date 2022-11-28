import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

blank = np.zeros((400,400),dtype='uint8')
# cv.imshow('blank',blank)

#rect
rectangle = cv.rectangle(blank.copy(),(30,30),(370,307),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('rect',rectangle)
cv.imshow('circle',circle)

#bitwise And
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('and',bitwise_and)

#bitwise or
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('or',bitwise_or)

#bitwise xor
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('xor',bitwise_xor)

#bitwise not
bitwise_not = cv.bitwise_not(circle)
cv.imshow('not',bitwise_not)

cv.waitKey(0)