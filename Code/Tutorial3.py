import cv2 as cv 

"""Basic Important Functions in open cv"""

"""1. Creating a grey scale img"""
img = cv.imread("Images/fuji.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Mount Fuji",img)
cv.imshow("Black Fuji",gray)
cv.waitKey(0)
"""--------------------------------------------------------------"""

"""2. Blur an image"""
img = cv.imread("Images/fuji.jpg")
blur_img = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Blured Image",blur_img)
cv.waitKey(0)
"""--------------------------------------------------------------"""

"""3. applying Canny edge detection """
img = cv.imread("Images/fuji.jpg") 
canny = cv.Canny(img,125,200) #simply for edge detection
dilate = cv.dilate(canny,(5,5),iterations=1) # for increasing edge thckness
eroded = cv.erode(dilate,(5,5),iterations=1) # to get the original edge of image
cv.imshow("canny Edge",eroded)
cv.waitKey(0)
"""--------------------------------------------------------------"""

"""4. Resizing and cropping image"""
img = cv.imread("Images/fuji.jpg")
img_resized = cv.resize(img,(400,400),interpolation=cv.INTER_CUBIC)
cropped = img_resized[50:200,:]
cv.imshow("Resized",cropped)
cv.waitKey(0)
"""--------------------------------------------------------------"""

