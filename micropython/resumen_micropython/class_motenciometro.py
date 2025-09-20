from machine import Pin, ADC
from time import sleep

class Potenciometro():
    def __init__(self,adc):
        self.pot = ADC(Pin(34))
        self.pot.atten(ADC.ATTN_11DB)    
        self.pot.width(ADC.WIDTH_12BIT)
    
    def Update(self):
        raw = self.pot.read()                        # Lectura bruta (0–4095)
        voltage = raw * (3.3 / 4095)            # Conversión a voltios
        return voltage
        sleep(0.5)
        
potenciometro = Potenciometro