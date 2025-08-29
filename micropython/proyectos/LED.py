from machine import Pin
from time import sleep

pin = Pin(32,Pin.OUT)# 2 es el de la esp32
stop = 0
while True:
    try:
        if stop == 2:
            respuesta = int(input("quieres detener el bucle(1=si y 2=no): "))#int(float(input("quieres detener el bucle(1=si y 2=no): ")))para conciderar numeros decimales
            if respuesta == 1:
                break
            elif respuesta == 2:
                stop = 0
        else:
            #pin.value(1)
            pin.on()
            print("on")
            sleep(1)
            #pin.value(0)
            pin.off()
            print("off")
            sleep(1)
            stop +=1
            print(f"vuelta {stop}")
    except:
        pass
    
    finally:
        pin.value(0)
#led: el + largo es el + y el + corto -
#Retorno a tierra (GND)