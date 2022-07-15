import cv2 as cv
path = input('provide path for the image')
try:
    image = cv.imread(path)
    frame = input('what do you want to be the frame name:')
    cv.imshow(frame, image)
    cv.waitKey(0)
except:
    print('enter the correct path')
