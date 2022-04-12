import numpy as np
import math as m
import matplotlib.pyplot as plt
import cv2

image = plt.imread('images/blur.jpeg')
plt.imshow(image)
plt.show()

image1 = np.copy(image)
i,j,l = 100, 100, 100
image1[i:i+j, j:j+l] = [255,0,0]
plt.imshow(image1)
plt.show()