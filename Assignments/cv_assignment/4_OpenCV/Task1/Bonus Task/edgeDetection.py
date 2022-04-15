import numpy as np
import cv2
video = cv2.VideoCapture(0)

while(video.isOpened()):
    _, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("GRAY image",gray)

    # Blur the image for better edge detection
    #img_blur = cv2.blur(gray, (5,5), 1)
    img_blur = cv2.GaussianBlur(gray, (19,19), 1)
    #img_blur = cv2.medianBlur(gray, ksize=13)
    cv2.imshow("Blur", img_blur)
    #cv2.waitKey(0)
    
    #blur = cv2.medianBlur(masked, 5)
    edged = cv2.Canny(img_blur, 20, 200)
    #edged = cv2.Sobel(img_blur, ddepth= -1, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
    cv2.imshow("Edge Detection",edged)
    

    contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame, contours, -1, (255,255,255), 2)
    cv2.imshow("Output",frame)

    if cv2.waitKey(10) == ord('x'):
        cv2.destroyAllWindows()
        video.release()
        break