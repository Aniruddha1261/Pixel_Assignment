#############Suboptimal implementation of convolution #####################
import cv2
import numpy as np
import matplotlib.pyplot as plt

def convolve(kernel, kernel1, orig_img):
    #################################################################
    img = cv2.copyMakeBorder(orig_img, 1, 1, 1, 1, cv2.BORDER_CONSTANT) # Add padding
    res_img = orig_img.copy()
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
                res_img[i - 1, j - 1] = np.sum((img[i - 1 : i + 2, j - 1 : j + 2] * kernel[:])*kernel1[:])
    return res_img
  
orig_img = cv2.imread("images/dog_test.png", 0) # Read Image
kernel = np.array([ 1/4,  1/2,  1/4]) # Simple vertical gradient kernel
kernel1 = np.array([[1/4],[1/2],[1/4]]) # Simple vertical gradient kernel
res = convolve(kernel, kernel1, orig_img)

orig = cv2.cvtColor(orig_img, cv2.COLOR_BGR2RGB)
plt.imshow(orig)
plt.show()
plt.imshow(res, cmap = plt.cm.gray)
plt.show()