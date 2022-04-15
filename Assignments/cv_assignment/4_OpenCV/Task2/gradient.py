import cv2
from cv2 import Sobel
import numpy as np

img = cv2.imread('images\example.JPG',0)
gradient = Sobel(img,ddepth=cv2.CV_64F, dx=1, dy=1, ksize=3)
cv2.imshow("Orignal", img)
cv2.imshow("Dialation", gradient)
cv2.waitKey(0)