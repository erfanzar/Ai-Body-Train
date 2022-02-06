import mediapipe as mp
import time
from mediapipe.python.solutions.drawing_utils import BLACK_COLOR
from mediapipe.python.solutions.pose import Pose 
import numpy as np
import cv2 
import math



key = cv2.waitKey(0)
mp_drawing = mp.solutions.mediapipe.python.solutions.drawing_utils
mp_drawing_styles = mp.solutions.mediapipe.python.solutions.drawing_styles
mp_pose = mp.solutions.mediapipe.python.solutions.pose
Pose = mp_pose.Pose()



def find(results , image):
        lmList = []
        if results.pose_landmarks:    
            for id , lm in enumerate(results.pose_landmarks.landmark):
                h,w,c = image.shape
                x,y = int(lm.x*w) , int(lm.y*h)
                lmList.append([id  , x ,y])
        return lmList     



def findangel(self , image , lmList,p1 ,p2 ,p3 , draw = True):
        
        x1 , y1 = lmList[p1][1:]
        x2 , y2 = lmList[p2][1:]
        x3 , y3 = lmList[p3][1:]
        ds = math.hypot(x1*x3+y1*y3)

        angle = math.degrees( math.atan2(y3-y2,x3-x2)-math.atan2(y1-y2,x1-x2))
        
        angle=int(angle)
        
        if angle<0:
         angle+=360

        if draw :
            cv2.circle(image,(x1,y1) ,10 , (0,255,0), cv2.FILLED)
            cv2.circle(image,(x1,y1) ,15 , (0,255,0), 1)

            cv2.putText(image,f'{int(angle)}' , (x3-50 , y2-50), cv2.FONT_HERSHEY_PLAIN,2,(255,0,0))

            cv2.circle(image,(x2,y2) ,15 , (0,255,0), cv2.FILLED)
            cv2.circle(image,(x2,y2) ,15 , (0,255,0), 1)
 
            cv2.circle(image,(x3,y3) ,15 , (0,255,0), cv2.FILLED)
            cv2.circle(image,(x3,y3) ,15 , (0,255,0), 1)

            cv2.line(image,(x1,y1) , (x3,y3) ,(255,255,255),2 ,cv2.FILLED)
            cv2.line(image,(x1,y1) , (x2,y2) ,(255,255,255),2 ,cv2.FILLED)
            cv2.line(image,(x2,y2) , (x3,y3) ,(255,255,255),2 ,cv2.FILLED)


        return angle