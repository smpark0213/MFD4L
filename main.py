from utils import *
import cv2

w, h = 1280, 720
pid = [0.5, 0.5, 0]
pError = 0
startCounter = 0

myDrone = initializeTello()

while True:
    if startCounter == 0:
        myDrone.takeoff()
        startCounter = 1

    img = telloGetFrame(myDrone, w, h)
    img, info = findHead(img)
    pError = trackHead(myDrone, info, w, pid, pError)
    print(info[0][0])

    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == 'q':
        myDrone.land()
        break