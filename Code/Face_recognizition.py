import cv2 as cv 
import numpy as np 

People = ["Joey","Chandler","Ross"]
haar_cascade = cv.CascadeClassifier('Xml/Haarcascade_face.xml')

Face_recognizer = cv.face.LBPHFaceRecognizer_create()
Face_recognizer.read('Data/Face_train.yml')

img = cv.imread('Images/Friends/Chandler/img2.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

Face_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
for (x,y,w,h) in Face_rect:
    Face_roi = gray[y:y+h,x:x+w]
    Label , Confidence = Face_recognizer.predict(Face_roi)
    cv.putText(img,People[Label],(20,20),cv.FONT_HERSHEY_PLAIN,1,(255,255,255),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),thickness=2)
cv.imshow('Person',img)
cv.waitKey(0)    
print(f'The person in the Image is {People[Label]}')

