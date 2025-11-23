# @mi_decorador
# def mi_funcion():
#     pass
# Esto es equivalente a:
# mi_funcion = mi_decorador(mi_funcion)

from functools import wraps
# y se aplica @wraps(func) dentro del decorador. 
# Así se conserva la identidad de la función original.

def decorador(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("➡️ Wrapper recibió:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper # 🔁 Reemplaza la función original,y esta es la razon por la que 
                   # definimos otra funcion
@decorador
def saludar(nombre, edad):
    print(f"Hola {nombre}, tenés {edad} años")

wrapper = saludar("Alejandro", 15)
print(wrapper)
