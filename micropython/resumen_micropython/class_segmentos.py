from machine import Pin

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
        
        self.P = None
        if Pin_P != None:
            self.P = Pin(Pin_P, Pin.OUT)
        
        
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
            if self.P != None and num == 0:
                self.P.on()
            else:
                self.P.off()
                
        
segmento = Segmento(16,2,32,12,13,25,14,27)

num = input("ingrese un numero de 1 a 9 :")
segmento.number(num)

            
            