import RPi.GPIO as GPIO
from time import sleep
dac = [21, 20, 16, 12, 25, 24, 23, 18]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def Funk(a):
    return [int(i) for i in bin(a)[2:].zfill(8)]
try:
    period = 3
    while True:
        # Плавный подъём от 0 до 255
        for a in range(256):
            GPIO.output(dac, Funk(a))
            sleep(period / 512) 
        for a in range(255, -1, -1):
            GPIO.output(dac, Funk(a))
            sleep(period / 512)
            
except KeyboardInterrupt:
    print("\nОстановлено")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

  