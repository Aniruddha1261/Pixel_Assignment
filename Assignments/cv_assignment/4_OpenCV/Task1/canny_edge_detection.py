import cv2
import numpy as np

image = cv2.imread("images\Emma.jpg")
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey Image", grey)

# Find Canny edges
edged = cv2.Canny(grey, 120, 230)
cv2.imshow("edged", edged)
cv2.waitKey(0)