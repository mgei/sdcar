import pygame
from pygame.locals import *
import cv2
import numpy as np
import sys

camera = cv2.VideoCapture(0)
pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")
screen = pygame.display.set_mode([640,480])

pygame.key.set_repeat(1, 10000)

try:
    while True:
        ret, frame = camera.read()
		
        screen.fill([0,0,0])
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0,0))
        pygame.display.update()

#        foc =  pygame.key.get_focused()
#        print(foc)
        
#        ipt = key_input = pygame.key.get_pressed()
#        print(ipt)

        gotinput = 0

        for event in pygame.event.get():
            gotinput = 1
            if event.type == KEYDOWN:
                key_input = pygame.key.get_pressed()

#                if key_input[pygame.K_UP] and key_input[pygame.K_RIGHT]:
#                    print("Forward Right")
#                elif key_input[pygame.K_UP] and key_input[pygame.K_LEFT]:
#                    print("Forward Left")
#                elif key_input[pygame.K_DOWN] and key_input[pygame.K_RIGHT]:
#                    print("Reverse Right")
#                elif key_input[pygame.K_DOWN] and key_input[pygame.K_LEFT]:
#                    print("Reverse Left")
                if key_input[pygame.K_UP]:
                    print("Forward")
                elif key_input[pygame.K_DOWN]:
                    print("Reverse")
                elif key_input[pygame.K_RIGHT]:
                    print("Right")
                elif key_input[pygame.K_LEFT]:
                    print("Left")
                elif key_input[pygame.K_x] or key_input[pygame.K_q]:
                    print("Stop")
                    sys.exit(0)

        if not gotinput:
            print("gotnoinout")

#sys.exit(0)

except (KeyboardInterrupt,SystemExit):
    pygame.quit()
    cv2.destroyAllWindows()
