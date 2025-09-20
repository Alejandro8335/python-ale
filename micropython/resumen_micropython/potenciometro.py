from machine import Pin, ADC
from time import sleep

# Configuración del ADC en GPIO 34
pot = ADC(Pin(34))

# Ajuste de rango de medida
pot.atten(ADC.ATTN_11DB)    # Permite medir hasta ~3.6 V sin saturar,Sin este paso, el rango por defecto (0–1 V) se saturaría al aplicar 3.3 V
pot.width(ADC.WIDTH_12BIT)  # Resolución de 12 bits: valores 0–4095

while True:
    raw = pot.read()                        # Lectura bruta (0–4095)
    voltage = raw * (3.3 / 4095)            # Conversión a voltios
    print(f"{raw} → {voltage}")
    sleep(0.5)
