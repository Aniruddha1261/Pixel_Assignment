#############Suboptimal implementation of convolution #####################
import cv2
import numpy as np
import matplotlib.pyplot as plt

def convolve(kernel, orig_img):
    #####################Flip kernel suboptimally####################
    kernel_inv = np.copy(kernel)
  #  print(kernel)
    for y in range(len(kernel)):
        kernel_inv[y] = kernel[len(kernel) - 1 -y]
    kernel_2 = np.copy(kernel_inv)
   # print(kernel_inv)
    for x in range(len(kernel[0])):
        kernel_inv[:,x] = kernel_2[:,len(kernel[0]) - 1 - x]
   # print(kernel_inv)
    #################################################################
    img = cv2.copyMakeBorder(orig_img, 1, 1, 1, 1, cv2.BORDER_CONSTANT) # Add padding
    res_img = orig_img.copy()
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
                res_img[i - 1, j - 1] = np.sum(img[i - 1 : i + 2, j - 1 : j + 2] * kernel_inv[:, :])
    return res_img
  
orig_img = cv2.imread("images/dog_test.png", 0) # Read Image
kernel = np.array([[ 1/16,  1/8,  1/16], [ 1/8,  1/4,  1/8], [ 1/16,  1/8,  1/16]]) # Simple vertical gradient kernel

res = convolve(kernel, orig_img)

orig = cv2.cvtColor(orig_img, cv2.COLOR_BGR2RGB)
plt.imshow(orig)
plt.show()
plt.imshow(res, cmap = plt.cm.gray)
plt.show()