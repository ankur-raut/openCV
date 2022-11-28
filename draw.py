import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype="uint8")
# cv.imshow('Blqnk',blank)

# img = cv.imread('Resources/Photos/cat.jpg')
# cv.imshow('cat',img)

# 1. paint the entier image
# blank[:] = 0,255,0
# cv.imshow('green',blank)

#2. rectangle
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0), thickness = -1)
# cv.imshow('rect',blank)

#3. circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness = -1)
cv.imshow('cir',blank)



cv.waitKey(0)