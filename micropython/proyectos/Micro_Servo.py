#cables :
#marron = tierra
#rojo = 5V
#amarillo = pin (donde va a ser la entrada de datos)

import machine
import time

frecuencia = 50
servo = machine.PWM(machine.Pin(5),frecuencia)

while True:
    for i in range(115,40,-1):
        servo.duty(i)
        print(i)
        time.sleep(0.05)	
    for i in range(41,115):
        servo.duty(i)
        print(i)
        time.sleep(0.05)