import cv2 as cv

image = cv.imread('New folder/prabhas.jpg')
cv.imshow('prabhas', image)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
# simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)
# inversing
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresh inverse', thresh_inv)

# adaptive thresholding
# C is the assumed mean
# threshold values based on mean
adapt = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 3)
cv.imshow('adapt', adapt)
cv.waitKey(0)