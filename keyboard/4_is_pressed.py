import keyboard
from time import sleep

print("Presioná los numeros para imprimir su valor. Esc para salir.")

run = True
while run:
    for i in range(10):
        i = str(i)
        if keyboard.is_pressed(str(i)):
            sleep(0.0575)
            if keyboard.is_pressed(str(i)):
                print(i)
    
    if keyboard.is_pressed('esc'):
        run = False