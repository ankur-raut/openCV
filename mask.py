import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('cat',img)


blank=np.zeros(img.shape[:2],dtype="uint8")
cv.imshow('Blqnk',blank)

# mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
# cv.imshow('mask',mask)

# masked = cv.bitwise_and(img,img,mask=mask)
# cv.imshow('masked',masked)

# weird
cir = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,-1)
rect = cv.rectangle(blank.copy(),(30,30),(370,307),255,-1)
#bitwise xor
bitwise_xor = cv.bitwise_xor(rect,cir)
cv.imshow('xor',bitwise_xor)

masked = cv.bitwise_and(img,img,mask=bitwise_xor)
cv.imshow('masked',masked)

cv.waitKey(0)