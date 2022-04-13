from cv2 import imread
import numpy as np
import math as m
import matplotlib.pyplot as plt
import cv2
# First convert your input rgb image to grayscale
image = cv2.imread('images/gradient.PNG', 0)
cv2.imshow('Grayscale Image', image)
cv2.waitKey(0)
'''# Then convert grayscale image to binary
thresh_img = cv2.threshold(image,130,255,cv2.THRESH_BINARY)[1]
cv2.imshow('BINARY', thresh_img)
cv2.waitKey(0)
print(np.array(thresh_img))
# Use this kernel'''
kernel = np.array([[0, 0, 1, 0, 0],[0, 1, 1, 1, 0],[1, 1, 1, 1, 1], [0, 1, 1, 1, 0],[0, 0, 1, 0, 0]])

def convolve(kernel, img1):
    img = cv2.copyMakeBorder(img1, 2, 2, 2, 2, cv2.BORDER_CONSTANT) # Add padding
    res_img = np.copy(img1)
    for i in range(2, img.shape[0] - 2):
        for j in range(2, img.shape[1] - 2):
            sum = np.sum(img[i - 2 : i + 3, j - 2 : j + 3] * kernel[:, :])
            #print(sum)
            if sum > 2760 :
                res_img[i - 2, j - 2] = 0
            elif sum <= 2760 and sum >= 255:
                res_img[i - 2, j - 2] = 255
            else:
                res_img[i - 2, j - 2] = 0
    return res_img

res = convolve(kernel, image)
#print(np.array(thresh_img))

orig = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#cv2.imshow('Original', orig)
#cv2.waitKey(0)
cv2.imshow('Dialated Image', res)
cv2.waitKey(0)