

import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BOARD)

on_button = 7
GPIO.setup(button, GPIO.IN)

s_led = 31
GPIO.setup(led, GPIO.OUT)

while True:
    
    if GPIO.input(button) == True:
        GPIO.output(led, True)
        print ("Boton ON!")
    
    else:
        GPIO.output(led, False)
        print ("Boton OFF!")
    
    time.sleep(0.2)
