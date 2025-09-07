#cables :
#marron = tierra
#rojo = 5V
#amarillo = pin (donde va a ser la entrada de datos)

import machine

frecuencia = 50
servo = machine.PWM(machine.Pin(5),frecuencia)

US_MIN = 500    # µs en 0°
US_MAX = 2400   # µs en 180°

def angle_to_pulse_us(angle):
    # a) Limita el rango de ángulo
    angle = max(0, min(180, angle))
    # b) Mapea 0–180° a 500–2400 µs
    return US_MIN + (angle / 180) * 1900#(US_MAX - US_MIN)

def pulse_us_to_duty(pulse_us, period_us=20000, resolution=1023):
    return int((pulse_us / period_us) * resolution)

while True:
    angle = int(input("angle: "))
    pulse = angle_to_pulse_us(angle)
    duty_value = pulse_us_to_duty(pulse)
    
    servo.duty(duty_value)
    
#RESUMEN
#ANGLE_TO_PULSE_US
    
#Convierte un ángulo (0–180°) en la duración del pulso en microsegundos (µs) que necesita el servo.

#Parámetros fijos:
#US_MIN = 500 µs → pulso para 0°
#US_MAX = 2400 µs → pulso para 180°
#Rango total de pulso = 1900 µs (2400 – 500) = (US_MAX - US_MIN)

#Mapear al rango de µs
#pulse_us = US_MIN + (angle / 180 * (US_MAX - US_MIN))
    
#proporción = angle / 180
#0° → 0
#90° → 0.5
#180°→ 1

#ejemplos
#angle = 0°
#pulse_us = 500 + (0/180)*1900 = 500 µs
    
#angle = 180°
#pulse_us = 500 + (180/180)*1900 = 2400 µs
    

#PULSE_US_TO_DUTY(pulse_us, period_us=20000, resolution=1023)

#Convierte la duración de pulso (µs) al valor de duty (0–1023) que acepta el PWM de MicroPython.
    
#Parámetros fijos:
#period_us = 20 000 µs → 50 Hz → ciclo completo de PWM
#resolution = 1023 → pasos posibles (10 bits)

#“100 % duty” usa 40 = → 40×500 µs = 20 000 µs alto constante.