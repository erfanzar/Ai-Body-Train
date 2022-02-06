
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





def alls(results , image):
        if results.pose_landmarks :
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                )