import numpy as np
import math as m
import matplotlib.pyplot as plt
import cv2

image = plt.imread('images/blur.jpeg')
plt.imshow(image)
#plt.show()
image1 = np.copy(image)
# x2 + y2 = r2
R = 50
r = 47
list_t = list(np. arange(0,361,0.01))
for t in list_t:
        if t < 90:
                image1[int(100-(R*np.sin(t))):int(100-(r*np.sin(t))),int(100-(r*np.cos(t))):int(100-(R*np.cos(t)))] = [255,0,0]
        elif t >= 90 and t < 180:
                image1[int(100-(R*np.sin(t))):int(100-(r*np.sin(t))),int(100-(R*np.cos(t))):int(100-(r*np.cos(t)))] = [255,0,0]
        elif t >= 180 and t < 270:
                image1[int(100-(r*np.sin(t))):int(100-(R*np.sin(t))),int(100-(R*np.cos(t))):int(100-(r*np.cos(t)))] = [255,0,0]
        else:
                image1[int(100-(r*np.sin(t))):int(100-(R*np.sin(t))),int(100-(r*np.cos(t))):int(100-(R*np.cos(t)))] = [255,0,0]
# for y in range(100, 201):
#         x = int(np.sqrt(int(np.square(y) - np.square(R))))
#         x2 = int(np.sqrt(int(np.square(y) - np.square(r))))
#         image1[y,x:x2] = [255,0,0]

plt.imshow(image1)
plt.show()