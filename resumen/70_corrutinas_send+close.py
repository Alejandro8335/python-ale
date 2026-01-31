def doble():
    x = 0
    while True: 
        x = (yield x * 2) # recibe un dato 

# Cuando una función tiene yield, no devuelve un valor final, 
# sino que se convierte en un generador.

# Al llamarla, no se ejecuta su cuerpo completo: solo se crea el objeto generador.

# Para empezar a correr el código, tenés que avanzar con next() o .send()

g = doble()
next(g)

# Cuando tenés una función con yield, se convierte en un generador.

# Ese generador puede recibir valores desde afuera usando el método .send(valor).

# El valor que mandás con .send() se convierte en el resultado de la expresión (yield) dentro de la función.

print(g.send(2))
print(g.send(3))
print(g.send(6))

g.close()
try:
    next(g)
except Exception as e:
    print(type(e), repr(e)) # <class 'StopIteration'> StopIteration()
    
# .close() termina el generador.

# Después de eso, cualquier avance da StopIteration.

# No ves nada porque esa excepción no tiene mensaje, pero sí se está lanzando.