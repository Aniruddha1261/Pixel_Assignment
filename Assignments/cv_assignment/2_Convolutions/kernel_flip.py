import cv2
import numpy as np
import matplotlib.pyplot as plt
def convolve(kernel, orig_img):
    #####################Flip kernel suboptimally####################
    kernel_inv = np.copy(kernel)
    i = len(kernel)
    j = len(kernel[0])
    print("Original Kernel")
    print(kernel)
    print(" ")
    for y in range(i):
        kernel_inv[y] = kernel[i - 1 -y]
    kernel_2 = np.copy(kernel_inv)
    print("Kernel after Rows Swap")
    print(kernel_inv)
    print(" ")
    for x in range(j):
        kernel_inv[:,x] = kernel_2[:,j - 1 - x]
    print("Kernel After Columns Swap")
    print(kernel_inv)
    #################################################################
    img = cv2.copyMakeBorder(orig_img, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value = 0) # Add padding
    res_img = orig_img.copy()
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
                res_img[i - 1, j - 1] = np.sum(img[i - 1 : i + 2, j - 1 : j + 2] * kernel_inv[:, :])
    return res_img

orig_img = cv2.imread("images/dog_test.png", 0) # Read Image
kernel = np.array([[ 1, 2, 3], [ 4, 5, 6], [ 7, 8, 9]]) # Simple vertical gradient kernel

res = convolve(kernel, orig_img)