import cv2 as cv
import numpy as np
blank = np.zeros((400, 400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (0, 50), (350, 350), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, thickness=-1)
cv.imshow('circle', circle)
cv.imshow('rectangle', rectangle)
bi_and = cv.bitwise_and(rectangle, circle)
cv.imshow('and', bi_and)
bi_or = cv.bitwise_or(rectangle, circle)
cv.imshow('or', bi_or)
bi_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('xor', bi_xor)
cv.waitKey(0)