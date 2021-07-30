import cv2 as cv
import numpy as np
import time
import os
import HandTrackingModule as htm

###########################

brushThickness = 15
eraserThickness= 100

###########################

folderPath=r"E:\pythonProject\OpenCv_project\Header"
myList =os.listdir(folderPath)
print(myList)
overlayLIst=[]
for i in myList:
    image=cv.imread(f'{folderPath}/{i}')
    overlayLIst.append(image)
print(len(overlayLIst))

header=overlayLIst[0]
drawcolor=(255,0,255)


cap=cv.VideoCapture(0)

cap.set(3, 1280)
cap.set(4, 720)

detector=htm.handDetector(detectionCon=0.85)
xp,yp=0,0
imgCanvas=np.zeros((720,1280,3),np.uint8)

#1.Import image
while True:
    sucesss,img =cap.read()

    img=cv.flip(img,1)

    #2.Find Handlandmark with the help of handDetection model

    img=detector.findHands(img)
    lmlist=detector.findPosition(img,draw=False)

    if len(lmlist)!=0:
        #print(lmlist)
        x1,y1=lmlist[8][1:] #Tip of index and middle finger
        x2,y2=lmlist[12][1:]


        #3.Check with fnger is up

        fingers=detector.fingersUP()
        #print(fingers)

        #4.if selection mode two fingers are up

        if fingers[1] and fingers[2]:
            xp,yp=0,0
            print("Selection Mode")
            #Checking for the click
            if y1 < 125 :
                if 250<x1<450:
                    header=overlayLIst[0]
                    drawcolor=(255,0,255)
                elif 550<x1<750:
                    header=overlayLIst[1]
                    drawcolor=(255,0,0)
                elif 800<x1<950:
                    header=overlayLIst[2]
                    drawcolor=(0,255,0)
                elif 1050<x1<1200:
                    header=overlayLIst[3]
                    drawcolor=(0,0,0)
            cv.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawcolor, cv.FILLED)


        #5.IF we are drawing mode index finger is up

        if fingers[1] and fingers[2]==False:
            cv.circle(img,(x1,y1),15,drawcolor,cv.FILLED)
            print("Drawing mode")
            #Lets drawing
            if xp==0 and yp==0:
                xp,yp=x1,y1

            if drawcolor==(0,0,0):
                cv.line(img, (xp, yp), (x1, y1), drawcolor, eraserThickness)
                cv.line(imgCanvas, (xp, yp), (x1, y1), drawcolor, eraserThickness)
            else:
                cv.line(img,(xp,yp),(x1,y1),drawcolor,brushThickness)
                cv.line(imgCanvas, (xp, yp), (x1, y1), drawcolor, brushThickness)

            xp,yp=x1,y1

    imgGray=cv.cvtColor(imgCanvas,cv.COLOR_BGR2GRAY)
    _, imgInv=cv.threshold(imgGray,50,255,cv.THRESH_BINARY_INV)
    imgInv=cv.cvtColor(imgInv,cv.COLOR_GRAY2BGR)
    img=cv.bitwise_and(img,imgInv)
    img=cv.bitwise_or(img,imgCanvas)



    #Setting the header image
    img[0:125, 0:1280]=header #Height and width of color plate
    #It is one way of adding two image and make trasparent 0.5
    #img=cv.addWeighted(img,0.5,imgCanvas,0.5,0)
    cv.imshow("IMGAE",img)
    cv.imshow("Canvas",imgCanvas)
    cv.imshow("Inv",imgInv)
    cv.waitKey(1)



