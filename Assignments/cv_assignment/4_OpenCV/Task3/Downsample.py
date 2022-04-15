import cv2
import numpy as np

image = cv2.imread("images\Emma.jpg", 0)
blur = cv2.pyrDown(image)
cv2.imshow("Original image", image)
cv2.imshow("Downsample image", blur)
cv2.waitKey(0)