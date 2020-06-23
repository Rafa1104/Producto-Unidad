##Correr este script despues de ejecutar en terminal lo siguiente:
##sudo socat -d -d -d -v -x PTY,link=/dev/ttyUSB10,mode=777,unlink-close,raw,echo=0 PTY,link=/dev/ttyUSB20,mode=777,unlink-close,raw,echo=0

##para leer la señal desde el puerto
##cat < /dev/ttyUSB10

import serial, time
from random import randrange, uniform

ser = serial.Serial('/dev/ttyUSB20', 9600)
print("emitiendo info ...")

while True:
    
    senalA=str(randrange(255))
    ser.write(str.encode(senalA)+str.encode('\n'))
    time.sleep(0.5)
    print(senalA)

    
    
