import numpy as np
import math as m
import matplotlib.pyplot as plt
import cv2

image = plt.imread('images/blur.jpeg')
plt.imshow(image)
#plt.show()
image1 = np.copy(image)
i = 100
R = 50
r = 47
for t in range(-90,90):
        if t < 90 and t > 0:
                image1[int(i-(R*np.sin(t))):int(i-(r*np.sin(t))),int(i + (r*np.cos(t))):int(i+(R*np.cos(t)))] = [255,0,0]
        elif t >= 90 and t < 180:
                image1[int(i-(R*np.sin(t))):int(i-(r*np.sin(t))),int(i - (R*np.cos(180-t))):int(i-(r*np.cos(180-t)))] = [255,0,0]
        elif t >= 180 and t < 270:
                image1[int(i-(R*np.sin(t))):int(i-(r*np.sin(t))),int(i + (R*np.cos(270-t))):int(i+(r*np.cos(270-t)))] = [255,0,0]
        elif t >= 270 and t <=360:
                image1[int(i-(R*np.sin(t))):int(i-(r*np.sin(t))),int(i - (r*np.cos(360-t))):int(i-(R*np.cos(360-t)))] = [255,0,0]
plt.imshow(image1)
plt.show()