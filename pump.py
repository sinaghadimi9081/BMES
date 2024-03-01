import time
import RPi.GPIO as GPIO
pumpR = 2
pumpL = 19
valveR = 13
valveL = 6
flex_basis = 0.4
flex_range = 0.1

GPIO.setmode(GPIO.BCM)
GPIO.setmode(pumpR,GPIO.OUT)
GPIO.setmode(pumpL,GPIO.OUT)
GPIO.setmode(valveR,GPIO.OUT)
GPIO.setmode(valveL,GPIO.OUT)

try:
    if -flex_basis >= flex_range:
        GPIO.output(pumpR,True)
        GPIO.output(pumpL,True)
        time.sleep(10)
        GPIO.output(pumpR,False)
        GPIO.output(pumpL,False)
        GPIO.output(valveR,True)
        GPIO.output(valveL,True)
        time.sleep(10)
except KeyboardInterrupt:
    print('Finish')