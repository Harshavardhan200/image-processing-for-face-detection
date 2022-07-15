import cv2 as cv
import numpy as np
def translate(image, x, y):
    trans = np.float32([[0, 1, x], [1, 0, y]])
    shape = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, trans, shape)
    # -x == left
    # -y == up
    # x == right
    # y == down
def rotate(image, rotationangle, rotpoint=None):
    (width, height) = image.shape[:2]
    dimensions = (width, height)
    if rotpoint is None:
        rotpoint = (width//2, height//2)
    rotmat = cv.getRotationMatrix2D(rotpoint, rotationangle, 1.0)
    return cv.warpAffine(image, rotmat, dimensions)

path = input('enter the path')
img = cv.imread(path)
inpu = input('do you want to transfer or rotate the image or fliping')
if inpu == 'transfer':
    x = int(input('enter x'))
    y = int(input('enter y'))
    transl = translate(img, x, y)
    cv.imshow('translate', transl)
elif inpu == 'rotate':
    angle = int(input('enter the angle'))
    rota = rotate(img, angle)
    cv.imshow('rotate', rota)
elif inpu == 'fliping':
    section = int(input('fliping vertically means 0, horizontally means 1 or both means -1'))
    flip = cv.flip(img, section)
    cv.imshow('flip', flip)
cv.waitKey(0)