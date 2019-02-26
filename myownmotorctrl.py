import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

pwm=GPIO.PWM(22, 100)

pwm.start(0)

GPIO.output(18, True)
GPIO.output(16, False)

pwm.ChangeDutyCycle(80)

GPIO.output(22, True)

time.sleep(2)

GPIO.output(22, False)

pwm.stop()
GPIO.cleanup()

