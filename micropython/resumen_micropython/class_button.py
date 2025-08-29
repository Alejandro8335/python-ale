from machine import Pin , PWM
from time import sleep_ms

class Button():
    def __init__(self,Pinn):
        self.Pin = Pin(Pinn, Pin.IN, Pin.PULL_UP)
        self.prev = False
    def Press(self):
        if not self.Pin.value()  and not self.prev:
            sleep_ms(80)
            if not self.Pin.value():
                self.prev = True
                return True
            
        elif self.Pin.value() and self.prev:
            sleep_ms(80)
            if self.Pin.value():
                self.prev = False

plus = Button(21)
minus = Button(23)
stop = Button(19)
led = PWM(Pin(32))
led.freq(90)
duty = 0
run = True
while run:
    led.duty(duty)
    if stop.Press():
        duty = 0
        led.duty(duty)
        run = False
        
    if plus.Press():
        duty += 205
        if duty >= 1023:
            duty = 1023
            print("\033[33mMAX \033[32mduty: 1023\033[0m")
        else:
            print(f"\033[32mvalor duty: {duty}\033[0m")
            
    if minus.Press():
        duty -= 205
        if duty <= 0:
            duty = 0
            print(f"\033[33mMIN \033[32mduty: 0\033[0m")
            
        else:
            print(f"\033[32mvalor duty: {duty}\033[0m")
            