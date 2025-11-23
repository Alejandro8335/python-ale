# *args
# Python los guarda en una tupla.
def sumar(*args):
    return sum(args)

print(sumar(1, 2, 3))       # 6
print(sumar(10, 20, 30, 40)) # 100

# **kwargs (keyword arguments)
# Python los guarda en un diccionario.
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        if clave == "nombre":
            print(valor)
        print(f"{clave}: {valor}")

mostrar_info(nombre="Alejandro", edad=25, ciudad="Rosario")
# nombre: Alejandro
# edad: 25
# ciudad: Rosario

# usando ambos juntos
def ejemplo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

ejemplo(1, 2, 3, nombre="Alejandro", edad=25)
# args: (1, 2, 3)
# kwargs: {'nombre': 'Alejandro', 'edad': 25}


# El nombre args o kwargs es solo una convención. Podrías usar cualquier otro nombre.
# * → indica que se reciben argumentos posicionales variables (se agrupan en una tupla).
# ** → indica que se reciben argumentos con nombre variables (se agrupan en un diccionario).