from cv2 import imread
import numpy as np
import math as m
import matplotlib.pyplot as plt
import cv2
# First convert your input rgb image to grayscale
image = cv2.imread('images/DK.jpeg', 0)
cv2.imshow('Grayscale Image', image)
cv2.waitKey(0)
# Then convert grayscale image to binary
thresh_img = cv2.threshold(image,128,255,cv2.THRESH_BINARY)[1]
cv2.imshow('BINARY', thresh_img)
cv2.waitKey(0)
print(np.array(thresh_img))
# Use this kernel
kernel = np.array([[0, 1, 0],[1, 1, 1],[0, 1, 0]])

def convolve(kernel, thres_img):
    img = cv2.copyMakeBorder(thresh_img, 1, 1, 1, 1, cv2.BORDER_CONSTANT) # Add padding
    res_img = np.copy(thresh_img)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            sum = np.sum(img[i - 1 : i + 2, j - 1 : j + 2] * kernel[:, :])
            #print(sum)
            if sum == 1275:
                res_img[i - 1, j - 1] = 255
            else:
                res_img[i - 1, j - 1] = 0
    return res_img

res = convolve(kernel, thresh_img)
#print(np.array(thresh_img))

orig = cv2.cvtColor(thresh_img, cv2.COLOR_BGR2RGB)
#cv2.imshow('Original', orig)
#cv2.waitKey(0)
cv2.imshow('Dialated Image', res)
cv2.waitKey(0)
