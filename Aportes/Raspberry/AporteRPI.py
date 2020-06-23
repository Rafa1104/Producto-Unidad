

import serial, time
from random import randrange, uniform

ser = serial.Serial('/dev/ttyUSB20', 9600)
print("emitiendo info ...")

while True:
    
    senalA=str(randrange(255))
    ser.write(str.encode(senalA)+str.encode('\n'))
    time.sleep(0.5)
    print(senalA)

    
    
