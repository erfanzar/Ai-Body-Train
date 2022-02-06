from tkinter import Y
import cv2 as cv
from matplotlib import scale 
import numpy as np
import math
from BodyAi import *




Net = cv.dnn.readNet('Ai Body/yolov4-tiny.weights' , 'Ai Body/yolov4-tiny.cfg')

Net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)

Net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

Model = cv.dnn_DetectionModel(Net)

Model.setInputParams(size=(416,416),swapRB= True , scale=1/255)


camera = cv.VideoCapture(0)


TrashHold = 0.3
TrashPass = 0.5

while True:
    grab , frame = camera.read()


    classes , scores , bboxs = Model.detect(frame,TrashHold , TrashPass)

    for (classid , score , bbox) in zip(classes , scores , bboxs ):
        x = int(bbox[0])
        y = int(bbox[1])
        w = int(bbox[2])
        h = int(bbox[3])


        cv.putText(frame , f'{classid}' , (x,y-20) , cv.FONT_ITALIC , 1 , (255,220,5),1)
        cv.rectangle(frame ,(x,y) , (x+h , w+y) ,(255,200,0),3)

        while classid == 0 :
            ai(camera)

    cv.imshow('result' , frame)

    cv.waitKey(1)

    if cv.waitKey(1) == ord('q'):
        break