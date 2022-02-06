import imp
import mediapipe as mp
import time
from mediapipe.python.solutions.drawing_utils import BLACK_COLOR
from mediapipe.python.solutions.pose import Pose 
import numpy as np
import cv2 
from findangle import *
from drawutils import *
from landmarkFinder import *
import math



########## imports


counte =0
key = cv2.waitKey(0)
mp_drawing = mp.solutions.mediapipe.python.solutions.drawing_utils
mp_drawing_styles = mp.solutions.mediapipe.python.solutions.drawing_styles
mp_pose = mp.solutions.mediapipe.python.solutions.pose
Pose = mp_pose.Pose()

# cap.set(3 , 640)
# cap.set(4, 480)




def ai(cap):



    dir = 0
    count = 0
    limit = 5

    minp = 0
    maxp = 1


    while True:


        success, image = cap.read()
        image  = cv2.resize(image,(640,480))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = Pose.process(image)

        

        cv2.rectangle(image ,(0,0) , (640,80) , (BLACK_COLOR) , cv2.FILLED)

        if count >= limit :
                cv2.putText(image , "That Might be Enought Be ready For Next Round" , (150,40) , cv2.FONT_HERSHEY_PLAIN ,1 , (0,0,255) , 2)        
        

        cv2.putText(image, f'{count} / {limit}' ,(20 , 40 ), cv2.FONT_HERSHEY_PLAIN ,1 ,(255,0,0) ,2) 
        
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    


        lmList = find(results , image)    

        
        if len(lmList)!=0:

            angle = findangel(findangel,image,lmList,12,14,16)
            print ("dreges :" ,angle , '  |  ' , "  Times :" , count)
            per = np.interp(angle,(220 , 310) ,(0,100))
            rc = np.interp(angle,(220,310),(250,100))
            rc=int(rc)
            if per == 100:
                if dir == 0:
                    count+=0.5
                    dir = 1
            if per == 0:
                if dir ==1:
                    count +=0.5
                    dir = 0
            
            cv2.rectangle(image ,(20 , 250) , (80 , 100) , (0,255,0),2)      
            cv2.rectangle(image ,(20 , 250) , (80 , rc) , (0,255,0),cv2.FILLED)               
            

        #   findangel(findangel,12,14,16)



        #pranoid= np.interp(ds,[250000 , 360000],[minp,maxp])
        #print (pranoid)
        #if pranoid< 0.3:
        #    counte = counte+1
        cv2.imshow('MediaPipe Pose', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()


