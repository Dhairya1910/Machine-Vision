import cv2 as cv 

""" *** This File Contains all Basic of reading an Image and scaling or resizing it *** """

""" Reading Basic Image """
img = cv.imread("Images/Cat2.jpeg")
cv.imshow("Cat",img)
cv.waitKey(0)
"""-----------------------------------------"""


"""Reading Videos in opencv"""
Capture = cv.VideoCapture("Videos/VALORANT   2023-08-13 14-00-35.mp4")
while True : 
    IsTrue , frame = Capture.read()
    cv.imshow("Video",frame)

    if cv.waitKey(1) == ord("d"):
        break
 
Capture.release()
cv.destroyAllWindows()
"""------------------------------------------"""


"""Reading a Live Video""" 
Cap = cv.VideoCapture(0)

while True:
    IsTrue , frame = Cap.read()
    cv.imshow("Live",frame)

    if cv.waitKey(1) == ord("q"):
        break

Cap.release()
cv.destroyAllWindows()
"""---------------------------------------------"""


"""Image and Video Scaling and Resizing """
def Rescaled_img(frame,scale=0.75):
    widht = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dim = (widht,height)

    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)

Cap = cv.VideoCapture("Videos/VALORANT   2023-08-13 14-00-35.mp4")
while True:
    IsTrue , frame = Cap.read()
    frame = Rescaled_img(frame)
    cv.imshow("Video",frame)
    if cv.waitKey(1) == ord("q"):
        break 

Cap.release()
cv.destroyAllWindows()
"""--------------------------------------------------"""

"""Resizing a Live Video"""
def changeRes(capture,width,height):
    capture.set(3,width)
    capture.set(4,height)
    return capture

Capture = cv.VideoCapture(0)
Capture_scaled = changeRes(Capture,400,200)

while True : 
    Is_True , frame = Capture.read()
    Is_True , Frame = Capture_scaled.read()

    cv.imshow("Original Frame",frame)
    cv.imshow("Rescaled Frame",Frame)

    if cv.waitKey(1) == ord("q"):
        break 
Capture.release()
cv.destroyAllWindows()
"""---------------------------------------------------"""






