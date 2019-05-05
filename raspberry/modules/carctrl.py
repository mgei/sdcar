import RPi.GPIO as GPIO
import pygame
import spidev
import time

class Car:   
    def __init__(self, fstate, bstate, rstate, lstate):
        self.fstate = fstate
        self.bstate = bstate
        self.rstate = rstate
        self.lstate = lstate
        
        self.drivemotor = [22, 18, 16] # enable, in1, in2
        self.steermotor = [15, 13, 11]
        self.triggerech = [12, 7]      # trigger, echo        

        self.llim = 370 # default values, may be changed once instance is created
        self.rlim = 640
        self.flim = 15 # forward limit distance in cm
        
        self.initialized = False
        
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
        
        # potentiometer for steering delimiter
        global spi
        spi = spidev.SpiDev()
        spi.open(0,0) 
        
        # ultrasonic
        GPIO.setup(self.triggerech[0], GPIO.OUT)
        GPIO.setup(self.triggerech[1], GPIO.IN)
  
        self.initialized = True
        
    def drive(self, direction, speed = 100):
        if not self.initialized:
            self.initialize()
        
        if direction == 'f':
            GPIO.output(self.drivemotor[1], True)
            GPIO.output(self.drivemotor[2], False)
            self.pwm_drive.start(speed)
        elif direction == 'b':
            GPIO.output(self.drivemotor[1], False)
            GPIO.output(self.drivemotor[2], True)
            self.pwm_drive.start(speed)
        elif direction == '':
            GPIO.output(self.drivemotor[1], False)
            GPIO.output(self.drivemotor[2], False)
            self.pwm_drive.stop()
            
    def steer(self, direction, speed = 100):
        if not self.initialized:
            self.initialize()
        
        if direction == 'l':
            GPIO.output(self.steermotor[1], True)
            GPIO.output(self.steermotor[2], False)
            self.pwm_steer.start(speed)
        elif direction == 'r':
            GPIO.output(self.steermotor[1], False)
            GPIO.output(self.steermotor[2], True)
            self.pwm_steer.start(speed)
        elif direction == '':
            GPIO.output(self.steermotor[1], False)
            GPIO.output(self.steermotor[2], False)
            self.pwm_steer.stop()
            print(self.potentiometer())
            
    def potentiometer(self, channel = 0):
        if not self.initialized:
            self.initialize()

        spi.max_speed_hz = 1350000
        adc = spi.xfer2([1,(8+channel)<<4,0])
        data = ((adc[1]&3) << 8) + adc[2]
        return data
        
    def limitleft(self):
        if self.potentiometer() < self.llim:
            return 1
        
    def limitright(self):
        if self.potentiometer() > self.rlim:
            return 1

    def ultrasonic(self):
        if not self.initialized:
            self.initialize()

        # set Trigger to HIGH
        GPIO.output(self.triggerech[0], True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.triggerech[0], False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(self.triggerech[1]) == 0:
            StartTime = time.time()

        # save time of arrival
        while GPIO.input(self.triggerech[1]) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        return distance

    def limitforward(self):
        #if self.ultrasonic() < self.flim:
        #    return 1
        return 0

    def forward(self):
        if self.limitforward():
            # it in limitforward, stop driving immediately
            print('stop go forward due to distance limit')
            self.drive(direction = '')
            self.fstate = 0
        else:
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
                self.drive(direction = '')
                self.bstate = 0
                print('go forward')
                self.drive(direction = 'f')
                self.fstate = 1
            elif self.fstate and self.bstate:
                # both true, should not happen
                print('error: going forward and backward at the same time')
                self.drive(direction = '')
            
    def backward(self):
        # check if already driving
        if not self.fstate and not self.bstate:
            # it's stationary, start going backward
            print('go backward')
            self.drive(direction = 'b')
            self.bstate = 1
        elif not self.fstate and self.bstate:
            # it's already going backward, do nothing
            pass
        elif self.fstate and not self.bstate:
            # it's currently going forward, stop that and go backward instead
            print('stop go forward')
            self.drive(direction = '')
            self.fstate = 0
            print('go backward')
            self.drive(direction = 'b')
            self.bstate = 1
        elif self.fstate and self.bstate:
            # both true, should not happen
            print('error: going forward and backward at the same time')
            self.drive(direction = '')
            
    def stopdrive(self):
        # check if actually driving
        if not self.fstate and not self.bstate:
            # it's stationary, as we want
            pass
        elif self.fstate and not self.bstate:
            # it's going forward, stop it
            print('stop go forward')
            self.drive(direction = '')
            self.fstate = 0
        elif not self.fstate and self.bstate:
            # it's going backward, stop it
            print('stop go backward')
            self.drive(direction = '')
            self.bstate = 0
        elif self.fstate and self.bstate:
            # both true, should not happen
            print('error: going forward and backward at the same time')
            self.drive(direction = '')
            
    def left(self):
        if self.limitleft():
            # it in leftlimit, stop steering left immediately
            print('stop steer left due to steering limit')
            self.steer(direction = '')
            self.lstate = 0
        else:
            # check if already steering
            if not self.lstate and not self.rstate:
                # it's not steering, start steering left
                print('steer left')
                self.steer(direction = 'l')
                self.lstate = 1
            elif self.lstate and not self.rstate:
                # it's already steering left, do nothing
                pass
            elif not self.lstate and self.rstate:
                # it's currently steering right, stop that and steer left instead
                print('stop steer right')
                self.steer(direction = '')
                self.rstate = 0
                print('steer left')
                self.steer(direction = 'l')
                self.lstate = 1
            elif self.lstate and self.rstate:
                # both true, should not happen
                print('error: steering both directions the same time')
                self.steer(direction = '')
            
    def right(self):
        if self.limitright():
            # it in leftlimit, stop steering right immediately
            print('stop steer right due to steering limit')
            self.steer(direction = '')
            self.rstate = 0
        else:
            # check if already steering
            if not self.lstate and not self.rstate:
                # it's not steering, start steering right
                print('steer right')
                self.steer(direction = 'r')
                self.rstate = 1
            elif not self.lstate and self.rstate:
                # it's already steering right, do nothing
                pass
            elif self.lstate and not self.rstate:
                # it's currently steering left, stop that and steer right instead
                print('stop steer left')
                self.steer(direction = '')
                self.lstate = 0
                print('steer right')
                self.steer(direction = 'r')
                self.rstate = 1
            elif self.lstate and self.rstate:
                # both true, should not happen
                print('error: steering both directions the same time')
                self.steer(direction = '')
            
    def stopsteer(self):
        # check if actually steering
        if not self.lstate and not self.rstate:
            # it's not steering, as we want
            pass
        elif self.lstate and not self.rstate:
            # it's steering left, stop it
            print('stop steer left')
            self.steer(direction = '')
            self.lstate = 0
        elif not self.lstate and self.rstate:
            # it's steering right, stop it
            print('stop steer right')
            self.steer(direction = '')
            self.rstate = 0
        elif self.fstate and self.bstate:
            # both true, should not happen
            print('error: steering both directions at the same time')
            self.steer(direction = '')
            
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
            
    def ignitionoff(self):
        self.drive(direction = '')
        self.steer(direction = '')
        GPIO.cleanup()
        
        self.initialized = False
