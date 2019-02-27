import RPi.GPIO as GPIO
import time
import pygame
from pygame.locals import *
import sys

from modules.carctrl import Car

toycar = Car(0,0,0,0)
#toy.move('', '')

pygame.display.set_caption("Empty Pygame")
screen = pygame.display.set_mode([640,480])

carryOn = 1

drive = Car(0,0,0,0)

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn=0
            toycar.ignitionoff()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:     # press X to exit
                carryOn = 0
                toycar.ignitionoff()

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

    time.sleep(0.033)

