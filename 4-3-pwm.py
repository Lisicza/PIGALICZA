import RPi.GPIO as GPIO
import sys
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
dac=[21, 20, 16, 12, 25, 24, 23, 18]
GPIO.setup(dac, GPIO.OUT, initial=GPIO.HIGH)
pwm=GPIO.PWM(2, 1000)
pwm.start(0)

try:
     while True:
        DutyCicle=int(input())
        pwm.ChangeDutyCycle(DutyCicle)
        voltage = DutyCicle * 3.3 / 100
        print("%.2f" % voltage)
finally:
    GPIO.output(2, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()   