import cv2 as cv

image = cv.imread('New folder/prabhas.jpg')
cv.imshow('prabhas', image)
# blurring techniques
# Averaging
blur = cv.blur(image, (3, 4))
cv.imshow('averaging', blur)
# guassian blur
guass = cv.GaussianBlur(image, (3, 3), 0)
cv.imshow('guass', guass)
# median blur
med = cv.medianBlur(image, 3)
cv.imshow('median blur',med)
# bilateral blurring
bil = cv.bilateralFilter(image, 5, 15, 15)
cv.imshow('bilateral', bil)
cv.waitKey(0)
