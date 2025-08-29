#cables :
#marron = tierra
#rojo = 5V
#amarillo = pin (donde va a ser la entrada de datos)

import machine
import time

frecuencia = 50
servo = machine.PWM(machine.Pin(5),frecuencia)

def pulse_us_to_duty(pulse_us, period_us=20000, resolution=1023):
    return int((pulse_us / period_us) * resolution)

US_MIN = 500    # µs en 0°
US_MAX = 2400   # µs en 180°

def angle_to_pulse_us(angle):
    # a) Limita el rango de ángulo
    angle = max(0, min(180, angle))
    # b) Mapea 0–180° a 500–2400 µs
    return US_MIN + (angle / 180) * 1900#(US_MAX - US_MIN)

while True:
    angle = int(input("angle: "))
    pulse = angle_to_pulse_us(angle)
    duty_value = pulse_us_to_duty(pulse)
    
    servo.duty(duty_value)
    