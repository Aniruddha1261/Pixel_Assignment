import numpy as np
import cv2
video = cv2.VideoCapture(0)

kernel = np.ones((7,7), np.uint8)

while(video.isOpened()):
    _, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("GRAY image",gray)

    binary = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)[1]
    img1 = cv2.dilate(binary, kernel, iterations=1)
    cv2.imshow("Orignal",frame)
    cv2.imshow('BINARY', binary)
    cv2.imshow('Dialation', img1)

    if cv2.waitKey(10) == ord('x'):
        cv2.destroyAllWindows()
        video.release()
        break