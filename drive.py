#import RPi.GPIO as GPIO
import time
import pygame
from pygame.locals import *
import sys
import cv2
import numpy as np

from modules.carctrl import Car


camera = cv2.VideoCapture(0)
pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")
screen = pygame.display.set_mode([640,480])

#pygame.key.set_repeat(1, 10000)

# initiate toycar
toycar = Car(0,0,0,0)
# once this is done, you can control it with toycar.move(), 
# e.g. toycar.move('f','') for going forward

# pygame.display.set_caption("Empty Pygame")
# screen = pygame.display.set_mode([640,480])

carryOn = 1

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn=0
            toycar.ignitionoff()
            cv2.destroyAllWindows()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:     # press X to exit
                carryOn = 0
                toycar.ignitionoff()
                cv2.destroyAllWindows()

    ret, frame = camera.read()

    screen.fill([0,0,0])
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)
    screen.blit(frame, (0,0))
    pygame.display.update()

    key_input = pygame.key.get_pressed()
    
    if key_input[pygame.K_UP] and key_input[pygame.K_RIGHT]:
        toycar.move('f', 'r')
    elif key_input[pygame.K_UP] and key_input[pygame.K_LEFT]:
        toycar.move('f','l')
    elif key_input[pygame.K_DOWN] and key_input[pygame.K_RIGHT]:
        toycar.move('b','r')
    elif key_input[pygame.K_DOWN] and key_input[pygame.K_LEFT]:
        toycar.move('b','l')
    elif key_input[pygame.K_UP]:
        toycar.move('f', '')
    elif key_input[pygame.K_DOWN]:
        toycar.move('b','')
    elif key_input[pygame.K_LEFT]:
        toycar.move('','l')
    elif key_input[pygame.K_RIGHT]:
        toycar.move('','r')
    else:
        toycar.move('','')

   # time.sleep(0.033)

