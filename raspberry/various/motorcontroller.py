import RPi.GPIO as GPIO
import pygame

class Car:
    
    def __init__(self, fstate, bstate, rstate, lstate):
        self.fstate = fstate
        self.bstate = bstate
        self.rstate = rstate
        self.lstate = lstate
        
        self.drivemotor = [22, 18, 16] # enable, in1, in2
        self.steermotor = [15, 13, 11]
        
        self.llim = 0.35 # default values, may be changed once instance is created
        self.rlim = 0.65
        
        self.initialized = 0
        
    def initialize(self):
        GPIO.setmode(GPIO.BOARD)
        
        # drive
        GPIO.setup(self.drivemotor[0], GPIO.OUT)
        GPIO.setup(self.drivemotor[1], GPIO.OUT)
        GPIO.setup(self.drivemotor[2], GPIO.OUT)
        
        self.pwm_drive = GPIO.PWM(self.drivemotor[0], 100)
        
        # steer
        GPIO.setup(self.steermotor[0], GPIO.OUT)
        GPIO.setup(self.steermotor[1], GPIO.OUT)
        GPIO.setup(self.steermotor[2], GPIO.OUT)
        
        self.pwm_steer = GPIO.PWM(self.steermotor[0], 100)
        
    def drive(self, direction, speeddrive = 80, speedsteer = 80):
        if self.direction == 'f':
            GPIO.output(self.drivemotor[1], True)
            GPIO.output(self.drivemotor[2], False)
            self.pwm_drive.start(speeddrive)
        elif self.direction == 'b':
            GPIO.output(self.drivemotor[1], False)
            GPIO.output(self.drivemotor[2], True)
            self.pwm_drive.start(speeddrive)
        elif self.direction == '':
            GPIO.output(self.drivemotor[1], False)
            GPIO.output(self.drivemotor[2], False)
            self.pwm_drive.stop()
        
    def steeringdelimitor(self):
        # if (lval < llim) or (rval > rlim):
            # stop steering
            # return 1
            pass
        
    def forward(self):
        # check if already driving
        if not self.fstate and not self.bstate:
            # it's stationary, start going forward
            print('go forward')
            self.drive(direction = 'f')
            self.fstate = 1
        elif self.fstate and not self.bstate:
            # it's already going forward, do nothing
            pass
        elif not self.fstate and self.bstate:
            # it's currently going backward, stop that and go forward instead
            print('stop go backward')
            self.bstate = 0
            print('go forward')
            self.fstate = 1
        elif self.fstate and self.bstate:
            # both true, should not happen
            print('error: going forward and backward at the same time')
            
    def backward(self):
        # check if already driving
        if not self.fstate and not self.bstate:
            # it's stationary, start going backward
            print('go backward')
            self.bstate = 1
        elif not self.fstate and self.bstate:
            # it's already going backward, do nothing
            pass
        elif self.fstate and not self.bstate:
            # it's currently going forward, stop that and go backward instead
            print('stop go forward')
            self.fstate = 0
            print('go backward')
            self.bstate = 1
        elif self.fstate and self.bstate:
            # both true, should not happen
            print('error: going forward and backward at the same time')
            
    def stopdrive(self):
        # check if actually driving
        if not self.fstate and not self.bstate:
            # it's stationary, as we want
            pass
        elif self.fstate and not self.bstate:
            # it's going forward, stop it
            print('stop go forward')
            self.fstate = 0
        elif not self.fstate and self.bstate:
            # it's going backward, stop it
            print('stop go backward')
            self.bstate = 0
        elif self.fstate and self.bstate:
            # both true, should not happen
            print('error: going forward and backward at the same time')
    
    def left(self):
        # check if already steering
        if not self.lstate and not self.rstate:
            # it's not steering, start steering left
            print('steer left')
            self.lstate = 1
        elif self.lstate and not self.rstate:
            # it's already steering left, do nothing
            pass
        elif not self.lstate and self.rstate:
            # it's currently steering right, stop that and steer left instead
            print('stop steer right')
            self.rstate = 0
            print('steer left')
            self.lstate = 1
        elif self.lstate and self.rstate:
            # both true, should not happen
            print('error: steering both directions the same time')
            
    def right(self):
        # check if already steering
        if not self.lstate and not self.rstate:
            # it's not steering, start steering right
            print('steer right')
            self.rstate = 1
        elif not self.lstate and self.rstate:
            # it's already steering right, do nothing
            pass
        elif self.lstate and not self.rstate:
            # it's currently steering left, stop that and steer right instead
            print('stop steer left')
            self.lstate = 0
            print('steer right')
            self.rstate = 1
        elif self.lstate and self.rstate:
            # both true, should not happen
            print('error: steering both directions the same time')
            
    def stopsteer(self):
        # check if actually driving
        if not self.lstate and not self.rstate:
            # it's not steering, as we want
            pass
        elif self.lstate and not self.rstate:
            # it's steering left, stop it
            print('stop steer left')
            self.lstate = 0
        elif not self.lstate and self.rstate:
            # it's steering right, stop it
            print('stop steer right')
            self.rstate = 0
        elif self.fstate and self.bstate:
            # both true, should not happen
            print('error: steering both directions at the same time')
            
    def move(self, drive, steer):
        if drive == 'f':
            self.forward()
        elif drive == 'b':
            self.backward()
        elif drive == '':
            self.stopdrive()
            
        if steer == 'l':
            self.left()
        elif steer == 'r':
            self.right()
        elif steer == '':
            self.stopsteer()
            
