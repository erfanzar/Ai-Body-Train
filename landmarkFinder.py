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

