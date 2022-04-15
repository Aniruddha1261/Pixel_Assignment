import cv2
import numpy as np

image = cv2.imread("images\Emma.jpg", 0)
blur = cv2.Sobel(image, cv2.CV_64F, 1, 1)

cv2.imshow("Original image", image)
cv2.imshow("Sobel image", blur)
cv2.waitKey(0)