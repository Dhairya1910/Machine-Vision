import cv2 as cv 
import numpy as np 

"""In This tutorial Contour detection method are discussed """

def Threshold_Contour_Detection(img):
    img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret , Thresh = cv.threshold(img,100,255,cv.THRESH_BINARY_INV)
    contour , hierarcy  = cv.findContours(Thresh,mode=cv.RETR_EXTERNAL,method=cv.CHAIN_APPROX_NONE)
    img = cv.drawContours(img,contour,-1,(0,0,255),2)
    return img 

     
def Canny_Contour_Detection(img):
    img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    canny = cv.Canny(img,125,175)
    contour , hierarcy = cv.findContours(canny,mode=cv.RETR_EXTERNAL,method=cv.CHAIN_APPROX_SIMPLE)
    print(contour)
    img = cv.drawContours(img,contour,-1,(0,255,75),2) 
    return img 

if __name__ == "__main__":

    img = cv.imread("Images/fuji.jpg")

    cv.imshow("Image with Threshold method",Threshold_Contour_Detection(img))
    cv.imshow("Image with Canny method",Canny_Contour_Detection(img))
    cv.waitKey(0)