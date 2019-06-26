import numpy as np
import cv2
"""
cap=cv2.VideoCapture(0)

_,frame=cap.read()
cv2.imshow("cap",frame)
"""
frame =cv2.imread("oct.jpg",1)
cv2.imshow("OCT",frame)

hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

# BLue
lower_color=np.array([90,80,90])        #hsv
upper_color=np.array([150,255,255])

mask=cv2.inRange(hsv,lower_color,upper_color)
res=cv2.bitwise_and(frame,frame,mask=mask)

cv2.imshow("MASK",mask)
cv2.imshow("Result",res)

# REd
lower_color1=np.array([0,80,90])        #hsv
upper_color1=np.array([30,255,255])

mask1=cv2.inRange(hsv,lower_color1,upper_color1)
res1=cv2.bitwise_and(frame,frame,mask=mask1)

cv2.imshow("MASK",mask1)
cv2.imshow("red",res1)

#Green


lower_color2=np.array([40,80,90])        #hsv
upper_color2=np.array([80,255,255])

mask2=cv2.inRange(hsv,lower_color2,upper_color2)
res2=cv2.bitwise_and(frame,frame,mask=mask2)

cv2.imshow("MASK",mask2)
cv2.imshow("green ",res2)


cv2.waitKey(0)
cv2.destroyAllWindows()