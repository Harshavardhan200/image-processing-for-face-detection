import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
image = cv.imread('New folder/prabhas.jpg')
cv.imshow('prabhas', image)
blank = np.zeros(image.shape[:2], dtype='uint8')
circle = cv.circle(blank, (image.shape[1]//2, image.shape[0]//4), 100, 255, -1)
masked = cv.bitwise_and(image, image, mask=circle)
cv.imshow('masked image', masked)
gray = cv.cvtColor(masked, cv.COLOR_BGR2GRAY)
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.plot(gray_hist)
plt.show()
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    cal = cv.calcHist([image], [i], circle, [256], [0, 256])
    plt.plot(cal)
plt.show()


cv.waitKey(0)