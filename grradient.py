import cv2 as cv
import numpy as np

image = cv.imread('New folder/prabhas.jpg')
cv.imshow('prabhas', image)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# lat pacing
lap = cv.Laplacian(gray, cv.CV_32F)
lap = np.uint8(np.absolute(lap))
cv.imshow('lapsian', lap)

#sabel
sabelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sabely = cv.Sobel(gray, cv.CV_64F, 0, 1)
sabel = cv.bitwise_or(sabelx, sabely)
cv.imshow('sobelx', sabelx)
cv.imshow('sobely', sabely)
cv.imshow('sabel', sabel)

# canny
canny = cv.Canny(image, 175, 250)
cv.imshow('canny', canny)
cv.waitKey(0)