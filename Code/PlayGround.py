import cv2 as cv 
import numpy as np 

"""playground to try and test different functions of opencv """
# capture = cv.VideoCapture(0)
# while True:
#     isTrue , frame = capture.read()
#     gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#     canny = cv.Canny(gray,50,255)
#     cv.imshow("real time Canny",canny)
#     if cv.waitKey(1) == ord('q'):
#         break 
# capture.release()
# cv.destroyAllWindows()

""" learning : Less the min thresh more the obj detected """
"""--------------------------------------------------------------"""

"""applying a adpative threshold to a live video"""
# Capture = cv.VideoCapture(0)
# while True:
#     isTrue , frame = Capture.read()
#     gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#     adp_thrsh = cv.adaptiveThreshold(gray_frame,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,7,3)

#     cv.imshow("heheh",adp_thrsh)

#     if cv.waitKey(1) == ord('q'):
#         break
# Capture.release()
# cv.destroyAllWindows()
"""--------------------------------------------------------------"""

"""application to capture only face of a human"""
# Capture = cv.VideoCapture(0)
# has_obj = cv.CascadeClassifier("Xml/Haarcascade_face.xml")
# while True:
#     isTrue , frame = Capture.read()
#     gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#     face_cords = has_obj.detectMultiScale(gray_frame,scaleFactor=1.1,minNeighbors=3)

#     for (x,y,w,h) in face_cords:
#         cv.rectangle(frame,(x,y),(x+w,y+h),color=(255,0,0),thickness=2)
#         if cv.waitKey(1) == ord("d"):
#             cropped = frame[y:y+h,x:x+w]
#             cv.imshow("Cropped",cropped)

#     cv.imshow("try",frame)
#     if cv.waitKey(1) == ord('q'):
#         print(frame.shape)
#         break 

# Capture.release()
# cv.destroyAllWindows()
"""--------------------------------------------------------------"""

"""Live video Contour detection"""
# Capture = cv.VideoCapture(0)
# while True:
#     isTrue , frame = Capture.read()
#     gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#     canny = cv.Laplacian(gray,ddepth=cv.CV_8UC1)
#     # contour , _ = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE) 
#     # Contour_img = cv.drawContours(frame,contour,-1,(0,0,255),2)
#     cv.imshow("Contour Video",canny)
#     if cv.waitKey(1) == ord("q"):
#         break 

# Capture.release()
# cv.destroyAllWindows()
"""--------------------------------------------------------------"""

