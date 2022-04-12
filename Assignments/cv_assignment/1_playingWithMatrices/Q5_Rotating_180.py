import numpy as np
import math as m
import matplotlib.pyplot as plt
import cv2

image = plt.imread('images/blur.jpeg')
plt.imshow(image)
#plt.show()
h,w,c=image.shape
image1=np.zeros((w,h,c),dtype=image.dtype)  # creating a new array for image
for i in range(h):
  for j in range(w):
    image1[i][j]=image[h-1-i][w-i-j] #clockwise rotation ke liye
    # image1[j][i]=image[i][j] #anti clockwise rotation + flip ke liye
plt.imshow(image1)
plt.show()