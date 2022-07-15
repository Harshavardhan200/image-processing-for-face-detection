import cv2 as cv
folder = input('Enter the folder')
file = input('Enter file name')
path = f'{folder}/{file}'
video = cv.VideoCapture(path)
while True:
    frame = video.read()
    cv.imshow('frame', frame[1])

    if 0xFF == ord('d') & cv.waitKey(20):
        break
video.release()
cv.destroyAllWindows()