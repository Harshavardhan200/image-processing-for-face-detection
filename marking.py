import cv2 as cv
import numpy as np

image = cv.imread('New folder/prabhas.jpg')
cv.imshow('prabhas', image)
blank = np.zeros(image.shape[:2], dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (image.shape[1]//2, image.shape[0]//2), (image.shape[1]//4, image.shape[0]//4), 255, -1)
circle = cv.circle(blank, (image.shape[1]//2, image.shape[0]//4), 100, 255, -1)
cv.imshow('rectangle', rectangle)
bi_and = cv.bitwise_and(rectangle, circle)
masked = cv.bitwise_and(image, image, mask=bi_and)
cv.imshow('masked image', masked)
cv.waitKey(0)