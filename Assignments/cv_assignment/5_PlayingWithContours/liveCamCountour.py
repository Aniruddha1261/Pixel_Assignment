import numpy as np 
import cv2
import imutils

video = cv2.VideoCapture(0)

while(video.isOpened()):
    _, frame = video.read()
    cv2.imshow("Image",frame)

    if cv2.waitKey(10) == 13:
        bbox = cv2.selectROI(frame)
        
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        obj_img = hsv[bbox[1]:bbox[1]+bbox[3],bbox[0]:bbox[0]+bbox[2]]

        h, s, v = np.median(obj_img[:,:,0]), np.median(obj_img[:,:,1]), np.median(obj_img[:,:,2])

        lower = np.array([h-5, max(0,s-50),max(0,v-50)])
        upper = np.array([h+5, min(s+50,255),min(v+50,255)])
        print(lower,upper)
        break


while(video.isOpened()):
    _, frame = video.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    masked = cv2.inRange(hsv, lower, upper)
    cv2.imshow("Masked", masked)
    blur = cv2.medianBlur(masked, 5)
    blob_mask = cv2.bitwise_and(frame,frame,mask=blur)

    cv2.imshow("blob_mask",blob_mask)
    cv2.waitKey(0)
    contours, _ = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont = imutils.grab_contours(contours)
    c = max(cont, key=cv2.contourArea)

    idx, current_max, counter = 0, 0, 0
    for n in contours:
        area = cv2.contourArea(n)
        if area > current_max:
            current_max = area
            idx = counter
        counter += 1

    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])

    # idx, current_max, counter = 0, 0, 0
    # for n in contours:
    #     area = cv2.contourArea(n)
    #     if area > current_max:
    #         current_max = area
    #         idx = counter
    #     counter += 1
    cv2.drawContours(frame, contours, idx, (0,255,255),2)
    cv2.circle(frame, extLeft, 8, (0, 0, 255), -1)
    cv2.circle(frame, extRight, 8, (0, 255, 0), -1)
    cv2.circle(frame, extTop, 8, (255, 0, 0), -1)
    cv2.circle(frame, extBot, 8, (255, 255, 0), -1)
    cv2.imshow("Output",frame)
    if cv2.waitKey(10) == ord('x'):
        cv2.destroyAllWindows()
        video.release()
        break