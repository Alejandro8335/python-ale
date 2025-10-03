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
    x = 25   # esto crea una variable local, no toca la global
    print("Dentro:", x)

f()
print("Fuera:", x)  # sigue siendo 10

# Resumen
# Sin global → la función crea su propia copia local, y al salir se pierde.

# Con global → la función trabaja directamente sobre la variable global, y los cambios persisten.
