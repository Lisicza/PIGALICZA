import RPi.GPIO as GPIO
import time
dac = [21, 20, 16, 12, 25, 24, 23, 18]
comp = 4
troyka = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

def decimal(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    for value in range(256):
        bits = decimal(value)
        GPIO.output(dac, bits)         
        time.sleep(0.001)              
        if GPIO.input(comp) == 1:       
            return value
    return 255  

try:
    while True:
        dig_val = adc()
        voltage = dig_val * 3.3 / 255.0
        print(f"Цифровое значение: {dig_val:3d}, напряжение: {voltage:.2f} В")
        time.sleep(0.1)  

finally:
    GPIO.output(dac, [0] * 8)
    GPIO.output(troyka, 0)
    GPIO.cleanup()        