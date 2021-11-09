import cv2
import numpy as np
def nothing(x):
    pass
cap=cv2.VideoCapture(0)  #starrting the web cam
cv2.namedWindow('Sketch') 
cv2.createTrackbar('Left','Sketch',0,255,nothing)
cv2.createTrackbar('Right','Sketch',0,255,nothing)

while True:
    ret,frame=cap.read()

    image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   #converting the image to gray scale
    image=cv2.GaussianBlur(image,(7,7),0)   #creating a gaussian blur of 7*7 kernel

    left=cv2.getTrackbarPos('Left','Sketch')     #getting the left position from the tracker
    right=cv2.getTrackbarPos('Right','Sketch')  #getting the right position from the tracker

    image=cv2.Canny(image,left,right)     #Canny Edge Detection Method

    #ret,image=cv2.threshold(image,50,255,cv2.THRESH_BINARY_INV)   #Creating a binary inverse threshold of the image 

    cv2.imshow("Original",frame)
    cv2.imshow("Sketch",image)

    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()