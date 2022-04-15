import numpy as np
import math as m
import matplotlib.pyplot as plt
import cv2

image = plt.imread('images/blur.jpeg')
plt.imshow(image)
#plt.show()
h,w,c=image.shape
thetha = input(print("Enter angle by which you want to rotate image : ", end= " "))
print(thetha)
image1=np.zeros((h,w,c),dtype=image.dtype)  # creating a new array for image

#centre of image 
cx = w/2
cy = h/2

for i in range(h):
  for j in range(w):
    #image1[i][j]=image[h-1-i][w-1-j] #clockwise rotation ke liye
    #distance of the pixal from centre

    #x-co-ordinate
    x = j - cx
    #y-co-ordinate
    y = i - cy
    #distance of the pixal from centre
    d = int(np.sqrt(np.square(x - cx) + np.square(y - cy)))
    image1[i][j]=image[int(d*np.sin(thetha))][int(d*np.cos(thetha))] #anti clockwise rotation + flip ke liye
    
    
plt.imshow(image1)
plt.show()