from machine import Pin
from time import sleep_ms

button = Pin(19, Pin.IN, Pin.PULL_UP)# 1 = sin pulsar, 0 = pulsado
led = Pin(32,Pin.OUT)
prev_pressed = False
on = False
while True:
    if not button.value()  and not prev_pressed:
        sleep_ms(80)
        if not button.value():
            on = not on
            led.value(on)
            print("on" if on else "off")
            prev_pressed = True
            
    elif button.value() and prev_pressed:
        sleep_ms(80)
        if button.value():
            prev_pressed = False
        
    