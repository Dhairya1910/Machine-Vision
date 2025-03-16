import cv2 as cv 
import numpy as np 
img = cv.imread("Images/fuji.jpg")

"""This file contains all the basic tranformation operation that can be performed on an image"""

"""1.Image Translation"""
def Translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
Translated_img = Translate(img,100,100)
cv.imshow("Image Translation",Translated_img)
cv.waitKey(0)
"""--------------------------------------------------------------"""

"""2.Image Rotation"""
def Rotate(img,angle,rotpoint=None):
    (width,height) = img.shape[0:2]
    if rotpoint is None:
        rotpoint = (width//2,height//2)
    RotMat = cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dim = (width,height)
    return cv.warpAffine(img,RotMat,dim)
rotated_img = Rotate(img,45)
cv.imshow("Rotation",rotated_img)
cv.waitKey(0)
"""--------------------------------------------------------------"""

"""3.Flipping an image"""
flipped_img = cv.flip(img,0)
cv.imshow("Flipped_img",flipped_img)
cv.waitKey(0)
"""--------------------------------------------------------------"""

"""4.Crop an image """
cropped_img = img[150:300,250:500]
cv.imshow("Cropped_img",cropped_img)
cv.waitKey(0)
"""---------------------------------------------------------------"""

"""5. Resize an Image"""
resized_img = cv.resize(img,(600,600),interpolation=cv.INTER_CUBIC)
cv.imshow("Resized",resized_img)
cv.waitKey(0)
"""--------------------------------------------------------------"""
