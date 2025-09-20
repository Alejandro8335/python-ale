from machine import Pin, ADC
from time import sleep

class Potenciometro():
    def __init__(self,adc_pin):
        self.pot = ADC(Pin(adc_pin))
        self.pot.atten(ADC.ATTN_11DB)    
        self.pot.width(ADC.WIDTH_12BIT)
    
    def Read_volts(self):
        raw = self.pot.read()                        
        sleep(0.5)
        return raw
    
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
                
def Volts_to_number(volts):
    return int(volts*9/4095)

potenciometro = Potenciometro(34)
segmento = Segmento(16,2,32,12,13,25,14,27)

while True:
    #volts = potenciometro.Read_volts()
    #number = Volts_to_number(volts)
    #segmento.number(number)
    segmento.number(Volts_to_number(potenciometro.Read_volts()))
