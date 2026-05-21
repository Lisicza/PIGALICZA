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
    value = 0
    for i in range(7, -1, -1):   
        candidate = value | (1 << i) #побитовый сдвиг влево
        bits = decimal(candidate)
        GPIO.output(dac, bits)
        time.sleep(0.001)   
        if GPIO.input(comp) == 1:
            pass
        else:
            value = candidate
    return value

try:
    GPIO.output(troyka, GPIO.HIGH)
    measure = 10
    total_time = 0
    
    for _ in range(measure):
        start = time.time()
        dig_val = adc()
        end = time.time()
        total_time += (end - start)
        voltage = dig_val * 3.3 / 255.0
        print(f"Цифровое значение: {dig_val:3d}, напряжение: {voltage:.2f} В, время: {(end-start)*1000:.2f} мс")
        time.sleep(0.5) 
    print(f"\nСреднее время одного измерения: {total_time/measurements*1000:.2f} мс")

finally:
    GPIO.output(dac, [0]*8)
    GPIO.output(troyka, 0)
    GPIO.cleanup()