import numpy as np
import cv2

def rotate(img,angle_of_rotation,centre,shape_img):

    #1.create rotation matrix with numpy array
    R = np.transpose(np.array([[np.cos(angle_of_rotation),-np.sin(angle_of_rotation)],
                            [np.sin(angle_of_rotation),np.cos(angle_of_rotation)]]))
    h,w = shape_img
    
    pivot_point_x =  centre[0]
    pivot_point_y = centre[1]
    
    image1 = np.zeros(img.shape,dtype='u1') 

    for i in range(h): #h = number of row
        for j in range(w): #w = number of col
            OrigCoordinates = np.array([[j - pivot_point_x],[i - pivot_point_y]])
            
            newCordinates = np.dot(R,OrigCoordinates)

            new_x = pivot_point_x + int(newCordinates[0])
            new_y = pivot_point_y + int(newCordinates[1])


            if (0 <= new_x <= w-1) and (0 <= new_y <= h-1): 
                image1[new_y,new_x] = img[i,j]

    return image1

angle = int(input(print("Angle to rotate image", end= " ")))
thetha = angle * (np.pi/180)
image = cv2.imread('images/blur.jpeg') 
h,w = image.shape[:2] 
x = int(w/2)
y = int(h/2)
centre = (x,y)
image2 = rotate(image,thetha,centre,(h,w))
cv2.imshow("original_img",image)
cv2.imshow("own_rotate_img",image2)
cv2.waitKey(0)