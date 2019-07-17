import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



frame =cv2.imread("IMG(104).jpg",1)

cv2.imshow("OCT",frame)
shp=frame.shape            # dimensions
print("Dimensions of image :",shp[0],shp[1])

hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


# Blue
lower_color=np.array([90,80,90])        #hsv
upper_color=np.array([150,255,255])

mask=cv2.inRange(hsv,lower_color,upper_color)
res=cv2.bitwise_and(frame,frame,mask=mask)

cv2.imshow("Blue MASK",mask)
cv2.imshow("Result",res)

# Red
lower_color1=np.array([0,80,90])        #hsv
upper_color1=np.array([30,255,255])

maskr=cv2.inRange(hsv,lower_color1,upper_color1)
res1=cv2.bitwise_and(frame,frame,mask=maskr)

cv2.imshow("Red MASK",maskr)
cv2.imshow("red",res1)

#Green


lower_color2=np.array([40,80,90])        #hsv
upper_color2=np.array([80,255,255])

mask2=cv2.inRange(hsv,lower_color2,upper_color2)
res2=cv2.bitwise_and(frame,frame,mask=mask2)

inv_mask=cv2.bitwise_not(mask)
resinv=cv2.bitwise_and(frame,frame,mask=inv_mask)

cv2.imshow("Green MASK",mask2)
cv2.imshow("green ",res2)


#Inverted Blue for Macular hole Detection

cv2.imshow("Inverted blue mask",inv_mask)
cv2.imshow("Inverted blue ",resinv)


count =0          # no of colored white pixels
breakc=0

for j in range(shp[1]):  # - is downwards
    for i in range(shp[0]-10):
        flag = 0
        if (maskr[i][j]==255):                      #in red mask if pixel is white(i.e redpixels)
            resinv[i][j] = (55, 55, 55)             #making the colored image gray
            for k in range(10):                     #check upto ten pixels above each red pixel
                #print(resinv[i][j+k])
                a=resinv[i-k][j]                    #blue to black mask
                #resinv[i-k][j] = (255, 255, 255)
                #print(a)
                if(a[0]==0 and a[1]==0 and a[2]==0):      # if black found in above 10 pixels
                    for l in range(10):                    # in 50 to 55 pixels above if not black
                        b=resinv[i - k - 40 - l][j]
                        #resinv[i - k - 40 - l][j]=(180,0,180)     #make purple 50 to 55
                        if not(b[0]==0 and b[1]==0 and b[2]==0):
                            resinv[i - k - 40 - l][j] = (200,100,200)          #make red
                            flag=1
                            break
                    if(flag==1):

                        break
                    else:
                        resinv[i - k][j] = (255, 255, 255)    #whichever are just above red and if pixel is black mak it gray
                        resinv[i - k-1][j] = (255, 255, 255)
                        count=count+1
                        break
            break                                           # once first red pixel found break

#plt.imshow(resinv)

print(count)


cv2.imshow("Macular hole detection ",resinv)
cv2.waitKey(0)
cv2.destroyAllWindows()
