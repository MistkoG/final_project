from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import sys
import imutils
import subprocess
import os
#Red light ON
subprocess.call('python /home/pi/cv_test/working/servo/red.py', shell=True)
# User supplied values 
cascPath = sys.argv[1]

# Creating Haar-cascade Detection
faceCascade = cv2.CascadeClassifier(cascPath)

# initializing the camera and grabbing a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (160, 120)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(160, 120))

# Warming up the camera
#time.sleep(0.1)
time.sleep(1)
lastTime = time.time()*1000.0
# Frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = 0 #flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    #print time.time()*1000.0-lastTime," Found {0} faces!".format(len(faces))
	print " Opening "
    lastTime = time.time()*1000.0
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.circle(image, (x+w/2, y+h/2), int((w+h)/3), (255, 255, 255), 1)
	#subprocess.call('raspistill -o tweet-pic.jpg', shell=True)
	#subprocess.call('bash /home/pi/cv_test/working/tw.sh', shell=True)
	subprocess.call('python /home/pi/cv_test/working/servo/ser2.py', shell=True)
	subprocess.call('python /home/pi/cv_test/working/servo/green.py', shell=True)
	#os.system('mpg123 -q 16983_1461335348.mp3')    
# show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    
	# if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
        
  
        

