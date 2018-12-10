from imutils import face_utils
from imutils.video import VideoStream


import dlib
import cv2

import time
import picamera
import numpy
import imutils
p = "/home/pi/Desktop/shape_predictor_68_face_landmarks.dat_2"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

#with picamera.PiCamera() as camera:
print("[INFO] starting video stream...")
    #vs = VideoStream(src=0).start()
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
 
# start the FPS counter
#fps = FPS().start()
while True:
    image = vs.read()
    image = imutils.resize(image, width=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
 
# loop over the face detections
    for (i, rect) in enumerate(rects):
    # determine the facial landmarks for the face region, then
    # convert the facial landmark (x, y)-coordinates to a NumPy
    # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
 
    # loop over the (x, y)-coordinates for the facial landmarks
    # and draw them on the image
        for (x, y) in shape:
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
 
# show the output image with the face detections + facial landmarks
    cv2.imshow("Output", image)
    key = cv2.waitKey(1) & 0xFF
 
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
 
    # update the FPS counter
    #fps.update()
    #fps.stop()
    cv2.destroyAllWindows()
    vs.stop()
   