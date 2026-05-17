import RPi.GPIO as GPIO
import sys
GPIO.setmode(GPIO.BCM) # нумерация Broadcom
dac=[26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
def Funk(a, n):
    return [int (elem) for elem in bin(a)[2:].zfill(n)]
try:
    while (True):
        a=input('input 0-255')
        if a=='q':
            sys.exit()
        elif a.isdigit() and 0 <= int(a) <= 255:
            GPIO.output(dac, Funk(int(a), 8))
            print("{:.4f}".format(int(a)/255*3.3))
        elif a.isdigit() and int(a) < 0:
            print('not positive')
        elif not a.isdigit():
            print('not a positive integer')
# обработка ошибок
except ValueError:
    print('this type is not allowed')
except KeyboardInterrupt:
    print('done')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()