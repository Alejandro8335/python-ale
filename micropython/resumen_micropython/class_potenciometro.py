from machine import Pin, ADC
from time import sleep

class Potenciometro():
    def __init__(self,adc_pin):
        self.pot = ADC(Pin(adc_pin))
        self.pot.atten(ADC.ATTN_11DB)    
        self.pot.width(ADC.WIDTH_12BIT)
        
        #no es necesario
        self.last = None
    
    def Read_volts(self):
        raw = self.pot.read()                        
        voltage = raw * (3.3 / 4095)
        sleep(0.5)#es muy inportante no sacar,si se requiere precision!!
        
        #no es necesario
        last = raw // 100
        if self.last != last:
            self.last = last
            return voltage
        
potenciometro = Potenciometro(34)

while True:
    voltage = potenciometro.Read_volts()
    #solo para la parte del update que se puede sacar
    if voltage:
        print(voltage)