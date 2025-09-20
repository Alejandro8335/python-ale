from machine import Pin, ADC ,PWM
from time import sleep

class Potenciometro():
    def __init__(self,adc_pin):
        self.pot = ADC(Pin(adc_pin))
        self.pot.atten(ADC.ATTN_11DB)    
        self.pot.width(ADC.WIDTH_12BIT)
    
    def Read_volts(self):
        raw = self.pot.read()                        
        voltage = raw * (3.3 / 4095)
        return voltage
        
potenciometro = Potenciometro(34)
led = PWM(Pin(4))
led.freq(90)
while True:
    voltage = potenciometro.Read_volts()
    three_simple = int((voltage*1023)/3.3)# 3.3 or 4095
    led.duty(three_simple)