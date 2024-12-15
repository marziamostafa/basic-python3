import cv2
cam=cv2.VideoCapture(0) # 0- indicator to if multiple camera

while True:
    _,frame=cam.read() # we don't need the 1st parameter, that's why blank
    cv2.imshow('my cam',frame) # windows name, frame
    cv2.waitKey(1)