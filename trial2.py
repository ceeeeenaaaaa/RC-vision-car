# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/haarcascade_frontalface_alt2.xml')
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  # show the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.6, minNeighbors=5)
    for (x, y, w, h) in faces:
        print(x,y,w,h)
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray = gray[y:y+h, x:x+w] #(ycord_start, ycord_end)
        roi_color = image[y:y+h, x:x+w]
        img_item="my-image.png"
        cv2.imwrite(img_item,roi_gray)
        cv2.imwrite(img_item,image)
    
    cv2.imshow("Frame", image)
        
 
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
 
    # if the `q` key was pressed, break from the loop
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break