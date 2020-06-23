

import lcddriver
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

lcd = lcddriver.lcd()

button1 = 7
GPIO.setup(button1, GPIO.IN)

cont=0

lcd.lcd_clear()
lcd.lcd_display_string("     HOLA!!     ", 1)
lcd.lcd_display_string(" Presiona boton ", 2)

time.sleep(1)

while True:
    
    if GPIO.input(button1) == True:
        cont+=1
        lcd.lcd_clear()
        lcd.lcd_display_string("Boton presionado", 1)
        lcd.lcd_display_string(str(cont)+" veces!", 2)

    time.sleep(0.2)
