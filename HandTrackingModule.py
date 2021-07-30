
""""
Download from my another hand tracking project
and some change it.

"""

#Module is use for using an handtracking code for various purpose
#In this project Handtracking code will work in With in class.So it can use for any other related projects

import cv2 as cv
import mediapipe as mp
import time

#1:Accessing my webcam

#Importing hand model

class handDetector():
    def __init__(self,mode=False,maxHand=2,detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.maxHand=maxHand
        self.detectionCon=detectionCon
        self.trackingCon=trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHand,self.detectionCon,
                                        self.trackingCon)  # Hand tracking model
        self.mpDraw = mp.solutions.drawing_utils  # Han# d drawing (Joining a points)model
        self.tipIds=[4,8,12,16,20]

    def findHands(self,img,draw=True):
        #Put Fps
        imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
        self.results=self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for i in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,i,self.mpHands.HAND_CONNECTIONS)  #mp.hand_connection use for draw a points

                #We dont need landmarks

        return img

    def findPosition(self,img,handNo=0,draw=True):
        self.lmList=[]
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                #print(id,lm) #Converting to pixel
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                #print(id, cx, cy)
                self.lmList.append([id,cx,cy])
                if draw:  # IF you want any hand landmark number put that
                    cv.circle(img, (cx, cy), 15, (255, 0, 255), cv.FILLED)
        return self.lmList

    def fingersUP(self):
        fingers=[]

        #Thumb
        if self.lmList[self.tipIds[0]][1] < self.lmList[self.tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4Fingers
        for i in range(1,5):
            if self.lmList[self.tipIds[i]][2] < self.lmList[self.tipIds[i]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers



def main():
    pTime = 0
    cTime = 0
    cap = cv.VideoCapture(0)
    detector=handDetector()

    # This object(mediapipe)use RGB images so we need to convert it

    while True:
        session, img = cap.read()
        img = detector.findHands(img)
        lmlist=detector.findPosition(img)
        if len(lmlist)!=0:
            print(lmlist[4]) #Any number you want finger number
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv.putText(img, str(int(fps)), (20, 70), cv.FONT_HERSHEY_SIMPLEX, 2,
                   (0, 255, 255), 1)
        cv.imshow("Image", img)

        cv.waitKey(1)







if __name__== "__main__":
    main()