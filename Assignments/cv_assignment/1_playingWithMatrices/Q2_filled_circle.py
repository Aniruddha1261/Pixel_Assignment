import numpy as np
import math as m
import matplotlib.pyplot as plt
import cv2

image = plt.imread('images/blur.jpeg')
plt.imshow(image)
#plt.show()
image1 = np.copy(image)
# (x-x0)^2 + (y-y0)^2 = r^2
i = 100
r = 50
for t in range(-90,90):
        image1[int(100 - (r*np.cos(t))):int(100+(r*np.cos(t))),int(100-(r*np.sin(t))):int(100+(r*np.sin(t)))] = [255,0,0]
plt.imshow(image1)
plt.show()