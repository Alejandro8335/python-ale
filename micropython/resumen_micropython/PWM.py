from machine import Pin,PWM

led = PWM(Pin(32))
led.freq(90)
#led.duty(511 )#0% = 0 y 100% = 1023

duty = 0
while True:
    try:
        led.duty(duty)
        respuesta = int(float(input("1 = off / 2 + duty / 3 - duty :")))
        
        if respuesta == 1:
            led.duty(0)
            break
        
        elif respuesta == 2:
            duty += 205
            if duty > 1023:
                duty = 1023
                
        elif respuesta == 3:
            duty -= 205
            if duty < 0:
                duty = 0
                
        if duty == 1023:
            print(f"\033[33mMAX \033[32mduty: {duty}\033[0m")
        elif duty == 0:
            print(f"\033[33mMIN \033[32mduty: {duty}\033[0m")
        else:
            print(f"\033[32mvalor duty: {duty}\033[0m")
    except Exception as e:
        print(f"\033[31m{e}\033[0m")
        
#¿Qué es PWM?
#PWM (Pulse Width Modulation) es una técnica donde generamos una señal digital que oscila entre alto y bajo a una frecuencia fija.

#Cada ciclo dura el mismo tiempo (por ejemplo, 20 ms en un servo de 50 Hz), pero la parte “alta” del ciclo puede variar en duración.

#Al cambiar solo el ancho del pulso (sin tocar la frecuencia), controlamos dispositivos como servos, LEDs y motores con precisión.

#¿Qué es “duty” o ciclo de trabajo?
#El “duty” (valor de duty cycle) indica qué porcentaje del ciclo total la señal está en alto.

#Si el duty es 0 % → siempre en bajo
#Si el duty es 50 % → mitad del tiempo en alto, mitad en bajo
#Si el duty es 100 % → siempre en alto

#En MicroPython para ESP32, ese porcentaje se expresa como un número entre 0 y 1023 (10 bits).