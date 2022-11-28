import cv2 as cv

# read Images

# img = cv.imread('Resources/Photos/cat.jpg')
# cv.imshow('cat',img)

def rescale(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimension = (width,height)

    return cv.resize(frame,dimension,interpolation = cv.INTER_AREA)


vid = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = vid.read()
    image = cv.flip(frame, 1)

    frame_resize = rescale(frame)

    cv.imshow('Video',image)
    cv.imshow('vid',frame_resize)

    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

vid.release()
cv.destroyAllWindows()


cv.waitKey(0)