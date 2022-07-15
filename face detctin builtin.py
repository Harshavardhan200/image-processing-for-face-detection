import os
import cv2 as cv
import numpy as np
people = ['prabhas', 'prabhu deva', 'Raghava', 'vijay']
DIR = "../../Pictures/New folder"

cascade = cv.CascadeClassifier('hear_face.xml')
features = []
labels = []
def create_train():
    for i in people:
        path = os.path.join(DIR, i)
        label = people.index(i)
        for j in os.listdir(path):
            im_read = cv.imread(os.path.join(path, j))
            gray = cv.cvtColor(im_read, cv.COLOR_BGR2GRAY)
            face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            for (x, y, h, t) in face:
                face_roi = gray[y:y+t, x:x+h]
                features.append(face_roi)
                labels.append(label)
create_train()
features = np.array(features, dtype='object')
labels = np.array(labels)
face_det = cv.face.LBPHFaceRecognizer_create()