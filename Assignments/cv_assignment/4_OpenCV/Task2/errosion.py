import cv2
import numpy as np

img = cv2.imread('images\example.JPG',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
cv2.imshow("Orignal", img)
cv2.imshow("Errosion", erosion)
cv2.waitKey(0)