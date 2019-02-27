import RPi.GPIO as GPIO
import time
import pygame
from pygame.locals import *
import sys

class Car:
    def __init__(self, fstate, bstate, rstate, lstate):
        self.fstate = 0
        self.bstate = 0
        self.rstate = 0
        self.lstate = 0

    def forward(self):
        if self.fstate == 0:
            print("going forward")
            self.fstate = 1
            
    def backward(self):
        if self.bstate == 0:
            print("backward")
            self.bstate = 1
    
    def right(self):
        if self.rstate == 0:
            print("right")
            self.rstate = 1

    def left(self):
        if self.lstate == 0:
            print("left")
            self.lstate = 1

pygame.display.set_caption("Empty Pygame")
screen = pygame.display.set_mode([640,480])

carryOn = 1

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn=0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:     # press X to exit
                carryOn = 0

    key_input = pygame.key.get_pressed()
    
    if key_input[pygame.K_UP] and key_input[pygame.K_RIGHT]:
        print("Forward Right")
    elif key_input[pygame.K_UP] and key_input[pygame.K_LEFT]:
        print("Forward Left")
    elif key_input[pygame.K_DOWN] and key_input[pygame.K_RIGHT]:
        print("Reverse Right")
    elif key_input[pygame.K_DOWN] and key_input[pygame.K_LEFT]:
        print("Reverse Left")
    elif key_input[pygame.K_UP]:
        print("Forward")
    elif key_input[pygame.K_DOWN]:
        print("Reverse")
    elif key_input[pygame.K_LEFT]:
        print("left")
    elif key_input[pygame.K_RIGHT]:
        print("right")
    else:
        print("no key")

    time.sleep(0.1)




#GPIO.setmode(GPIO.BOARD)
#
#GPIO.setup(22, GPIO.OUT)
#GPIO.setup(18, GPIO.OUT)
#GPIO.setup(16, GPIO.OUT)
#
#pwm=GPIO.PWM(22, 100)
#
#pwm.start(0)
#
#GPIO.output(18, True)
#GPIO.output(16, False)
#
#pwm.ChangeDutyCycle(80)
#
#GPIO.output(22, True)
#
#time.sleep(2)
#
#GPIO.output(22, False)
#
#pwm.stop()
#GPIO.cleanup()
#
