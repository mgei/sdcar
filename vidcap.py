#import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

#cap.set(cv2.CAP_PROP_FPS, 10)

#fps = cap.get(cv2.CAP_PROP_FPS)

#print(fps)

#cap.set(cv2.CAP_PROP_FPS, 3)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #time.sleep(1)
    #cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) + 10)
    #cap.set(cv2.CAP_PROP_FPS, 5) #this will cause the camera to freeze, reboot required after!

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the resulting frame
    # cv2.imshow('frame',gray)
    # cv2.imshow('frame',color)
    #k = cv2.waitKey(1000) # 0means waits forever for a keystroke

    cv2.imshow('frame', frame)
    k = cv2.waitKey(1) # 0 means waits forever for a keystroke
    if k & 0xFF == ord('q'):
        break
#    else:
#        print(k)
#    time.sleep(0.1) #works but doesn't improve streaming speed

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

