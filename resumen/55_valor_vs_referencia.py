# Conceptos básicos
# En Python, una variable no contiene el objeto, sino una referencia a él.

# Dos variables pueden apuntar al mismo objeto en memoria.

# Lo importante es distinguir entre:

# Modificar el objeto (si es mutable, el cambio se ve en todas las referencias).
# (obj,list y set) # son obj dinamicos

# Reasignar la variable (la variable apunta a otro objeto, 
# pero las demás referencias siguen igual).

x = 15
y = x
print (f"x: {x}: {id(x)}; y: {y}: {id(y)}")
x += 1 # cambia la referencia pq los obj int no son mutables
print (f"x: {x}: {id(x)}; y: {y}: {id(y)}")

#####################################################
z = 20; k = 20 # comparte id pq python los junta
print (f"z: {z}: {id(z)}; k: {k}: {id(k)}")

w = [1,2,3]; f = [1,2,3] # no comparten id pq son obj mutables
print (f"w: {w}: {id(w)}; f: {f}: {id(f)}")
#####################################################
a = [1, 2]
b = a          # b apunta al mismo objeto que a
print(f"a: {id(a)}; b: {id(b)}")  # mismo id → misma referencia

b.append(3)    # modificamos el objeto
print(f"a: {a}")    # [1, 2, 3] → se ve el cambio en a

b = []         # ahora b apunta a un objeto nuevo
print(f"a: {id(a)}; b: {id(b)}")  # distinto id → ya no comparten objeto

# Asignación dentro de una función (x = ...) → 
# crea una variable local (a menos que uses global o nonlocal).
# los argumentos que resibe son los obj globales no hace un copia osea que contienen la misma id

# Modificar atributos o elementos (obj.atributo = ..., lista.append(...)) → 
# no cambia la referencia, sino el objeto original.

# Asignación dentro de un bucle (i = []) → solo cambia la variable i, 
# no afecta otros objetos fuera del bucle.