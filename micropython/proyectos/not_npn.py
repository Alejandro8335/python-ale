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

colector = Pin(4, Pin.OUT)
base = Pin(5, Pin.OUT)

btn_cltr = Button(15)
btn_base = Button(19)

colector.off()
base.off()
state_cltr = False
state_base = False
while True:
    if btn_cltr.Press():
        if not state_cltr:
            colector.on()
            state_cltr = True
            print("colector on")
        else:
            colector.off()
            state_cltr = False
            print("colector off")
    if btn_base.Press():
        if not state_base:
            base.on()
            state_base = True
            print("base on")
        else:
            base.off()
            state_base = False
            print("base off")