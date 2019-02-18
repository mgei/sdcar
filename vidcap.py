import numpy as np
import cv2
#import time

cap = cv2.VideoCapture(0)

#cap.set(cv2.CAP_PROP_FPS, 3)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #time.sleep(1)

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the resulting frame
    # cv2.imshow('frame',gray)
    # cv2.imshow('frame',color)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

