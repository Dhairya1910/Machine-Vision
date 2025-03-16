import cv2 as cv 
import numpy as np 

""" This tutorial file shows how to draw on an img using opencv """

blank = np.zeros((500,500,3),dtype="uint8")

""" 1. Coloring the image"""
blank[200:400,200:400] = 0,200,0
cv.imshow("img",blank)
cv.waitKey(0)
"""--------------------------------------------------------------"""

""" 2. Creating a Rectangle and a circle """
cv.rectangle(blank,(50,50),(100,100),(0,255,255),thickness=-1)
cv.circle(blank,(250,250),100,thickness=-1,color=(255,0,0))
cv.imshow("Rectangle",blank)
cv.waitKey(0)
"""--------------------------------------------------------------"""

""" 3. Creating a Line """
cv.line(blank,(100,100),(200,200),thickness=3,color=(255,0,255))
cv.imshow("Line",blank)
cv.waitKey(0)
"""--------------------------------------------------------------"""

"""4. Putting a Text on the image""" 
cv.putText(blank,"S1mple",(200,250),cv.FONT_HERSHEY_SIMPLEX,1.0,(255,0,0))
cv.imshow("Text",blank)
cv.waitKey(0)
"""--------------------------------------------------------------"""

"""6. Practice """
white = np.ones((500,500,3),dtype="uint8")

cv.rectangle(white,(100,100),(200,200),color=(0,0,255),thickness=-1)
cv.rectangle(white,(300,100),(400,200),color=(0,0,255),thickness=-1)

cv.circle(white,(250,250),radius=100,color=(0,0,255),thickness=-1)

cv.line(white,(100,300),(300,300),color=(0,0,255),thickness=3)

cv.putText(white,text="S1mple",org=(250,100),fontFace=cv.FONT_HERSHEY_PLAIN,fontScale=1.0,color=(255,255,255))

cv.imshow("Practice",white)

cv.waitKey(0)
"""--------------------------------------------------------------"""