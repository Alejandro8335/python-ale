#creando una funcion que sume numeros
def Sumar_dos():
    #iniciando el bucle
    while True:
        #pidiendo numeros
        a = input("numero 1: ")
        b = input("numero 2: ")
        #intentando convertirlos a enteros y sumarlos
        try:
            resultado = int(a) + int(b)
        #si lanza una excepcion, pedirle que reingrese los datos
        except Exception as e:  
            print("Por favor, ingresa números enteros válidos.") 
            print(f"ERROR: {e}")
        #si todo salio bien terminamos el bucle
        else:
            break
        #el finally se ejecuta siempre 
        finally:
            print("esto se ejecuta siempre")
    return resultado

print(Sumar_dos())

#El bloque try en Python se usa para manejar excepciones 
#y evitar que el programa se detenga abruptamente cuando ocurre un error.
#Básicamente,le dice a Python: "Intenta ejecutar este código, pero si hay un error, 
#haz algo al respecto en lugar de simplemente fallar".

#Exception es la clase padre de todas las execiones(ValueError,ZeroDivisionError,etc)