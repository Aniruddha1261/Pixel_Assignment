from cv2 import imread
import numpy as np
import math as m
import matplotlib.pyplot as plt
import cv2
                            #####Dialation####
def dialation(kernel, thres_img):
    img = cv2.copyMakeBorder(thres_img, 2, 2, 2, 2, cv2.BORDER_CONSTANT) # Add padding
    res_img = np.copy(thres_img)
    for i in range(2, img.shape[0] - 2):
        for j in range(2, img.shape[1] - 2):
            sum = np.sum(img[i - 2 : i + 3, j - 2 : j + 3] * kernel[:, :])
            #print(sum)
            if sum >= 255:
                res_img[i - 2, j - 2] = 255
            else:
                res_img[i - 2, j - 2] = 0
    cv2.imshow("Dialation", res_img)
    cv2.waitKey(0)
    return res_img

                            #####ERROSION#####
def errosion(kernel, ans1):
    img = cv2.copyMakeBorder(ans1, 2, 2, 2, 2, cv2.BORDER_CONSTANT) # Add padding
    res_img = np.copy(ans1)
    for i in range(2, img.shape[0] - 2):
        for j in range(2, img.shape[1] - 2):
            sum = np.sum(img[i - 2 : i + 3, j - 2 : j + 3] * kernel[:, :])
            #print(sum)
            if sum == 3315:
                res_img[i - 2, j - 2] = 255
            else:
                res_img[i - 2, j - 2] = 0
    cv2.imshow("Errosion", res_img)
    cv2.waitKey(0)
    return res_img

                            ####Opening####
def opening(kernel, thres_img):
    ans1 = dialation(kernel, thres_img)
    ans2 = errosion(kernel, ans1)
    
    return ans2

# First convert your input rgb image to grayscale
image = cv2.imread('images\closing.PNG', 0)
#cv2.imshow('Grayscale Image', image)
#cv2.waitKey(0)
# Then convert grayscale image to binary
thresh_img = cv2.threshold(image,128,255,cv2.THRESH_BINARY)[1]
#cv2.imshow('BINARY', thresh_img)
#cv2.waitKey(0)
# Use this kernel
kernel = np.array([[0, 0, 1, 0, 0],[0, 1, 1, 1, 0],[1, 1, 1, 1, 1], [0, 1, 1, 1, 0],[0, 0, 1, 0, 0]])

res = opening(kernel, thresh_img)
cv2.imshow('Opening', res)
cv2.waitKey()