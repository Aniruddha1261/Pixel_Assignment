import numpy as np
import cv2
import imutils

img = cv2.imread("images\contour_input.jpeg")
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(grey, 50, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=2)

blur = cv2.GaussianBlur(grey, (5, 5), 0)
edge = cv2.Canny(blur, 50, 150)

con = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(con)
c = max(cont, key=cv2.contourArea)


extLeft = tuple(c[c[:, :, 0].argmin()][0])
extRight = tuple(c[c[:, :, 0].argmax()][0])
extTop = tuple(c[c[:, :, 1].argmin()][0])
extBot = tuple(c[c[:, :, 1].argmax()][0])

res = cv2.drawContours(image= img.copy(), contours= [c],contourIdx= -1,color= (0,255,0), thickness= 2)
res = cv2.circle(res, extLeft, 8, (0, 0, 255), -1)
res = cv2.circle(res, extRight, 8, (0, 255, 0), -1)
res = cv2.circle(res, extTop, 8, (255, 0, 0), -1)
res = cv2.circle(res, extBot, 8, (255, 255, 0), -1)

cv2.imshow("Original image", img)
cv2.imshow("grey image", grey)
cv2.imshow("Binary image", thresh)
cv2.imshow("Canny edge detection", edge)
cv2.imshow("Result",res)
cv2.waitKey(0)