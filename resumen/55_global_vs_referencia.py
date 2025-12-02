# Conceptos básicos
# En Python, una variable no contiene el objeto, sino una referencia a él.

# Dos variables pueden apuntar al mismo objeto en memoria.

# Lo importante es distinguir entre:

# Modificar el objeto (si es mutable, el cambio se ve en todas las referencias).

# Reasignar la variable (la variable apunta a otro objeto, 
# pero las demás referencias siguen igual).

a = [1, 2]
b = a          # b apunta al mismo objeto que a
print(id(a), id(b))  # mismo id → misma referencia

b.append(3)    # modificamos el objeto
print(a)       # [1, 2, 3] → se ve el cambio en a

b = []         # ahora b apunta a un objeto nuevo
print(id(a), id(b))  # distinto id → ya no comparten objeto

# Asignación dentro de una función (x = ...) → 
# crea una variable local (a menos que uses global o nonlocal).

# Modificar atributos o elementos (obj.atributo = ..., lista.append(...)) → 
# no cambia la referencia, sino el objeto original.

# Asignación dentro de un bucle (i = []) → solo cambia la variable i, 
# no afecta otros objetos fuera del bucle.