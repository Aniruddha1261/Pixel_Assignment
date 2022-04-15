import numpy as np
import cv2
video = cv2.VideoCapture(0)

while(video.isOpened()):
    _, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("GRAY image",gray)

    binary = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)[1]
    img3 = cv2.Sobel(binary,cv2.CV_64F,1,1,ksize=7)
    #img3 = cv2.Laplacian(binary,cv2.CV_64F)

    cv2.imshow("Orignal",frame)
    cv2.imshow('BINARY', binary)
    cv2.imshow('Gradient', img3)

    if cv2.waitKey(10) == ord('x'):
        cv2.destroyAllWindows()
        video.release()
        break