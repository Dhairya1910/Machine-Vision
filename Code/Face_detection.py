import cv2 as cv 

"""Simple Face detection from an image """
# img = cv.imread("Images/RV.jpg")
# cv.imshow("Rohit",img)
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("Gray Image",gray)

# haar_casc = cv.CascadeClassifier("Xml/Haarcascade_face.xml")

# facr_rect = haar_casc.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=3)

# for (x,y,w,h) in facr_rect:
#     cv.rectangle(img,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)

# cv.imshow("detected_img",img)
# cv.waitKey(0)
"""--------------------------------------------------------------"""

"""advance Face Detection using real time video"""
# cap = cv.VideoCapture(0)

# Har_obj = cv.CascadeClassifier("Xml/Haarcascade_face.xml")

# while True:
#     istrue , frame = cap.read()
#     gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

#     face = Har_obj.detectMultiScale(gray_frame,scaleFactor=1.5,minNeighbors=3)

#     for (x,y,w,h) in face:
#         cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),thickness=2)

#     cv.imshow("riyal time video",frame)

#     if cv.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv.destroyAllWindows()
"""--------------------------------------------------------------"""

