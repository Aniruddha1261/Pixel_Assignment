import cv2
from cv2 import blur
import numpy as np

image = cv2.imread("images\Emma.jpg")
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey Image", grey)
# Gaussian Blur
img_blur = cv2.GaussianBlur(grey, (19,19), 1)
cv2.imshow("Gausian Blur", img_blur)
#Blur
img1 = cv2.blur(grey, (19,19), 1)
cv2.imshow("Blur", img1)
#Median
img2 = cv2.medianBlur(grey, ksize=3)
cv2.imshow("Median Blur", img2)
#Bilateral
img3 = cv2.bilateralFilter(grey, 200,80,80)
cv2.imshow("Bilateral", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()