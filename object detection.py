import cv2 as cv
import numpy as np
path = input('enter the path')
image = cv.imread(path)
cv.imshow('image', image)
blank = np.zeros(image.shape, dtype='uint8')

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(image, (3, 3), cv.BORDER_DEFAULT)
ret, threshold = cv.threshold(gray, 152, 255, cv.THRESH_BINARY)
countors, hierachy = cv.findContours(threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(blank, countors, -1, (0, 254, 21), 2)
cv.imshow('blank', blank)
cv.waitKey(0)