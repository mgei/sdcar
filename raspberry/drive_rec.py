#import RPi.GPIO as GPIO
import time
import pygame
from pygame.locals import *
import sys
import cv2
import numpy as np
import csv

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
i = 1

logfile = 'test_img/log.csv'

with open(logfile, "w", 1) as result: # last argument is buffering, 1 = line buffering
        result.write("i; throttle; steering; potentio\n")
    
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

            cv2.imwrite('test_img/img' + str(i) + '.png', frame)

            #screen.fill([0,0,0])
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #frame = np.rot90(frame)
            #frame = cv2.flip(frame, 0)
            #frame = pygame.surfarray.make_surface(frame)
            #screen.blit(frame, (0,0))
            #pygame.display.update()

            key_input = pygame.key.get_pressed()
            
            if key_input[pygame.K_UP] and key_input[pygame.K_RIGHT]:
                toycar.move('f', 'r')
                throttle = 1
                steerinp = 1
            elif key_input[pygame.K_UP] and key_input[pygame.K_LEFT]:
                toycar.move('f','l')
                throttle = 1
                steering = -1
            elif key_input[pygame.K_DOWN] and key_input[pygame.K_RIGHT]:
                toycar.move('b','r')
                throttle = -1
                steering = 1
            elif key_input[pygame.K_DOWN] and key_input[pygame.K_LEFT]:
                toycar.move('b','l')
                throttle = -1
                steering = -1
            elif key_input[pygame.K_UP]:
                toycar.move('f', '')
                throttle = 1
                steering = 0
            elif key_input[pygame.K_DOWN]:
                toycar.move('b','')
                throttle = -1
                steering = 0
            elif key_input[pygame.K_LEFT]:
                toycar.move('','l')
                throttle = 0
                steering = -1
            elif key_input[pygame.K_RIGHT]:
                toycar.move('','r')
                throttle = 0
                steering = 1
            else:
                toycar.move('','')
                throttle = 0
                steering = 0

            potentio = toycar.potentiometer()

            result.write(str(i)+";"+str(throttle)+";"+str(steering)+";"+str(potentio)+"\n")

            i += 1

           # time.sleep(0.033)

