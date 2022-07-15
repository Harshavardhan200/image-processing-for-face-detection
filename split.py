import cv2 as cv
import numpy as np

image = cv.imread('New folder/prabhas.jpg')
cv.imshow('prabhas', image)
b,g,r = cv.split(image)

merge = cv.merge([b, g, g])
cv.imshow('merge', merge)
cv.waitKey(0)