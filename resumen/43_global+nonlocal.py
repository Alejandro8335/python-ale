# sin global
x = 10

def f():
    x = 20   # esto crea una variable local, no toca la global
    print("Dentro:", x)

f()
print("Fuera:", x)  # sigue siendo 10

# con global
x = 10

def f():
    global x
    x = 25   # esto toca la global ,no crea una variable local
    print("Dentro:", x)

f()
print("Fuera:", x)  # 25

# Resumen
# Sin global → la función crea su propia copia local, y al salir se pierde.

# Con global → la función trabaja directamente sobre la variable global, y los cambios persisten.


x = "global"

def exterior():
    x = "exterior"

    def interior():
        nonlocal x   # usa la x de exterior
        x = "interior"
        print("Dentro:", x) # Dentro: interior

    interior()
    print("Fuera:", x) # Fuera: interior

exterior()
print("Global:", x) # Global: global

# dentro de una funcion(def)
# = dentro de una función → crea variable local.

# global → modifica la variable del módulo.

# nonlocal → modifica la variable de la función envolvente.