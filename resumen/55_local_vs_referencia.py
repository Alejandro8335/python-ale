# En Python, todas las variables son referencias a objetos en memoria. 
# Pero hay una diferencia entre:

# Modificar el objeto al que apunta la variable (afecta el original si es mutable).

# Reasignar la variable a otro objeto (no afecta el original).

a = [1, 2]
b = a
print(id(a), id(b))  # 👉 mismo id → misma referencia

b.append(3)
print(a)  # 👉 [1, 2, 3] → se modificó el original

b = []
print(id(a), id(b))  # 👉 distinto id → ya no comparten objeto


# Entonces, ¿cómo saber si una variable es “local” o si tiene referencia real?

# Si estás dentro de una función y hacés x = algo, estás creando una variable local 
# (a menos que uses global o nonlocal).

# Si accedés a un atributo de un objeto (obj.atributo) y lo modificás sin reasignar, 
# estás modificando el objeto original.

# Si hacés i = [] dentro de un for, solo estás cambiando la variable i, 
# no el objeto original.