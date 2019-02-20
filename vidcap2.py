#import numpy as np
import cv2
#import time

#cap = cv2.VideoCapture(0)

#cap.set(cv2.CAP_PROP_FPS, 1)

#fps = cap.get(cv2.CAP_PROP_FPS)

#print(fps)

#cap.set(cv2.CAP_PROP_FPS, 3)

while(True):
    # Capture frame-by-frame
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    #time.sleep(1)
    
    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the resulting frame
    # cv2.imshow('frame',gray)
    # cv2.imshow('frame',color)
    k = cv2.waitKey(1) # 0 means waits forever for a keystroke

    cv2.imshow('frame', frame)
    if k & 0xFF == ord('q'):
        break
#    else:
#        print(k)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

