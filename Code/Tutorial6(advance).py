import cv2 as cv 
import numpy as np 


"""spliting an image into multiple channels"""
# img = cv.imread("Images/fuji.jpg")
# blank = np.zeros(img.shape[:2],dtype="uint8")
# print(blank)
# B,G,R = cv.split(img)
# print("the shape of Blue ",B.shape)
# print("the shape of Green ",G.shape)
# print("the shape of Red ",R.shape)
# print("the shape of Original ",img.shape)
# blue_img = cv.merge([B,blank,blank])
# cv.imshow("Blue Image",blue_img)
# cv.waitKey(0)
"""--------------------------------------------------------------"""

"""Smoothing an Image using different techniques"""
# img = cv.imread("Images/fuji.jpg")
# img = cv.resize(img,(255,255))
# # 1. Averaging Blur
# blurred_img = cv.blur(img,(5,5))
# # 2. Gaussian Blur
# Gauss_img = cv.GaussianBlur(img,(5,5),1)
# # 3. Median Blur 
# Median_img = cv.medianBlur(img,5)
# # 4. Bilateral Blur 
# Bilateral_img = cv.bilateralFilter(img,5,15,20)

# cv.imshow("Original",img)
# cv.imshow("Average Blur",blurred_img)
# cv.imshow("Gaussian Blur",Gauss_img)
# cv.imshow("Median Blur",Median_img)
# cv.imshow("Bilateral Blur",Bilateral_img)
# cv.waitKey(0)
"""--------------------------------------------------------------"""

"""Masking an image"""
# img = cv.imread("Images/fuji.jpg")

# blank = np.zeros(img.shape,dtype="uint8")
# mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,(250,250,250),-1)


# masked_img = cv.bitwise_and(img,mask)
# blurred = cv.blur(img,(5,5))

# portrait_img = cv.bitwise_or(blurred,masked_img)

# cv.imshow("creating mask",mask)
# cv.imshow("masked_img",masked_img)
# cv.imshow("Portrait Image",portrait_img)
# cv.imshow("Original",img)

# cv.waitKey(0)
"""--------------------------------------------------------------"""

"""Computing histogram"""


