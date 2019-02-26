import l293d
import gpiozero
import time


motor1 = l293d.DC(22, 18, 16)
motor2 = l293d.DC(15, 13, 11)

#motor1.anticlockwise(duration = 1)
motor2.anticlockwise(duration = 0.5)

l293d.cleanup()

