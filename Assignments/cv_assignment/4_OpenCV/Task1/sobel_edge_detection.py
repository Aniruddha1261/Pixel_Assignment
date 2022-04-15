import cv2
import numpy as np

image = cv2.imread("images\Sobel.PNG")
#grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Grey Image", grey)
#cv2.waitKey(0)

binary = cv2.threshold(image,100,255,cv2.THRESH_BINARY)[1]
cv2.imshow("Bianry image", binary)
cv2.waitKey(0)

# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(image, (11,11), 1)
cv2.imshow("Gausian Blur", img_blur)
cv2.waitKey(0)

# Sobel Edge Detection
sobelx = cv2.Sobel(img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(img_blur, ddepth= -1, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
# Display Sobel Edge Detection Images
#cv2.imshow('Sobel X', sobelx)
#cv2.waitKey(0)
#cv2.imshow('Sobel Y', sobely)
#cv2.waitKey(0)
cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
cv2.waitKey(0)
