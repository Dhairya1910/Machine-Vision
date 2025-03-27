import os 
import cv2 as cv 
import numpy as np 

People = ["Joey","Chandler","Ross"]
DIR = r'D:\Machine Vision\Images\Friends'
haar_cascade = "Xml/Haarcascade_face.xml"
model = cv.CascadeClassifier(haar_cascade)
Features = []
Labels = []


def create_train():
    for person in People:
        path = os.path.join(DIR,person)
        label = People.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            img_arr = cv.imread(img_path)
            gray = cv.cvtColor(img_arr,cv.COLOR_BGR2GRAY)

            face_rect = model.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)

            for (x,y,w,h) in face_rect:
                face_roi = gray[x:x+w,y:y+h]
                Features.append(face_roi)
                Labels.append(label)
            

create_train()

print('------------------------------------------')
print(f'Length of Feature list : {len(Features)}')
print(f'Length of labels list {len(Labels)}')
print('-------------------------------------------')
print('training completed--------------')

Features = np.array(Features,dtype='object')
Labels = np.array(Labels)

Face_reconizer = cv.face.LBPHFaceRecognizer_create()
Face_reconizer.train(Features,Labels)

np.save('Data/Features.npy',Features)
np.save('Data/Labels.npy',Labels)
Face_reconizer.save('Data/Face_train.yml')
print("----Files Successfully save into Data Folder----")
