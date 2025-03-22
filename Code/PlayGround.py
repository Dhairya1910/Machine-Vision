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

Capture = cv.VideoCapture(0)
while True:
    isTrue , frame = Capture.read()
    gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    adp_thrsh = cv.adaptiveThreshold(gray_frame,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,7,3)

    cv.imshow("heheh",adp_thrsh)

    if cv.waitKey(1) == ord('q'):
        break
Capture.release()
cv.destroyAllWindows()