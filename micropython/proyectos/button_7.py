from machine import Pin
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
                
class Segmento():
    def __init__(self,Pin_A,Pin_B,Pin_C,Pin_D,Pin_E,Pin_F,Pin_G,Pin_P = None):
        self.lista = [
            Pin(Pin_A, Pin.OUT),
            Pin(Pin_B, Pin.OUT),
            Pin(Pin_C, Pin.OUT),
            Pin(Pin_D, Pin.OUT),
            Pin(Pin_E, Pin.OUT),
            Pin(Pin_F, Pin.OUT),
            Pin(Pin_G, Pin.OUT),
        ]
        
        self.Pin_P = None
        if Pin_P != None:
            self.Pin_P = Pin(Pin_P, Pin.OUT)
        
        
    def number(self,num):
        patterns = [
        (1,1,1,1,1,1,0),  # 0 
        (0,1,1,0,0,0,0),  # 1
        (1,1,0,1,1,0,1),  # 2
        (1,1,1,1,0,0,1),  # 3
        (0,1,1,0,0,1,1),  # 4
        (1,0,1,1,0,1,1),  # 5
        (1,0,1,1,1,1,1),  # 6
        (1,1,1,0,0,0,0),  # 7
        (1,1,1,1,1,1,1),  # 8
        (1,1,1,1,0,1,1),  # 9
        ]
        
        num = max(0, min(int(num), 9))
        
        for Pin, state in zip(self.lista,patterns[num]):
            Pin.value(state)
            if self.Pin_P:
                if num == 0:
                    self.Pin_P.on()
                else:
                    self.Pin_P.off()
           

segmento = Segmento(16,2,32,12,13,25,14,26)
plus = Button(21)
minus = Button(23)
stop = Button(19)
counter = 0
run = True
while run:
    segmento.number(counter)
    
    if stop.Press():
        for Pin in segmento.lista:
            Pin.off()
        if segmento.Pin_P:
            segmento.Pin_P.off()
        run = False
        
    if plus.Press():
        counter += 1
        
    if minus.Press():
        counter -= 1
        
    if counter > 9:
        counter = 0
    
    if counter < 0:
        counter = 9
     