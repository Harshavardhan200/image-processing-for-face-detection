import cv2 as cv
edit = input('Do you want to resize video or photo')
def resize(frame1, scale=0.75):
    width = int(frame1.shape[1]*scale)
    height = int(frame1.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame1, dimensions, interpolation=cv.INTER_AREA)
if edit == 'photo':
    path = input('Enter the path')
    image = cv.imread(path)
    frame = input('what do you want to be the frame name:')
    frame_resize = resize(image)

    cv.imshow(frame, image)
    cv.imshow('resized photo', frame_resize)
    cv.waitKey(0)
elif edit == 'video':
    path = input('Enter the path')
    video = cv.VideoCapture(path)
    video_name = input('enter the frame name')
    while True:
        isTrue, frame = video.read()
        frame_resize = resize(frame)

        cv.imshow(video_name, frame)
        cv.imshow('resized', frame_resize)
