import cv2 as cv

image = cv.imread('New folder/group.jpg')
cv.imshow('prabhas', image)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cascade = cv.CascadeClassifier('hear_face.xml')
face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
print(len(face))
try:
    for (x,y,h, t) in face:
        cv.rectangle(image, (x, y), (x+h, y+t), (0, 255, 0), thickness=3)
except:
    pass
cv.imshow('prabhas', image)
cv.waitKey(0)