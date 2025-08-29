import machine
import time

pin = machine.Pin(2, machine.Pin.OUT)# 2 es el de la esp32

for i in range(5):
    #pin.value(1)
    pin.on()
    print("on")
    time.sleep(1)
    pin.value(0)
    print("off")
    time.sleep(1)
    print(i + 1)
#led: el + largo es el + y el + corto -
#Retorno a tierra (GND)