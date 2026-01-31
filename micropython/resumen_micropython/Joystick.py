# Pin Joystick	Conectar a
# VCC → 3.3V o 5V (según placa)
# GND → GND
# VRx → ADC Pin (por ejemplo, Pin(34) en ESP32)
# VRy → ADC Pin (Pin(35))
# SW → Digital Pin (Pin(32))

from machine import ADC, Pin
import time

# Configuración de los ejes
adc_x = ADC(Pin(34))
adc_x.atten(ADC.ATTN_11DB)   # rango ~0-3.6V
adc_x.width(ADC.WIDTH_12BIT) # 0-4095

adc_y = ADC(Pin(35))
adc_y.atten(ADC.ATTN_11DB)
adc_y.width(ADC.WIDTH_12BIT)

# Pulsador
sw = Pin(32, Pin.IN, Pin.PULL_UP)  # PULL_UP porque normalmente está abierto

while True:
    x = adc_x.read()   # 0-4095
    y = adc_y.read()   # 0-4095
    button = sw.value()  # 1 = suelto, 0 = presionado

    # Normalizar a -1 a 1
    x_norm = (x - 2048)/2048
    y_norm = (y - 2048)/2048

    print("X:", x_norm, "Y:", y_norm, "SW:", button)

    time.sleep(0.1) 