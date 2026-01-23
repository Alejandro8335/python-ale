# is chequea que dos valores compartan id (id(x) == id(y))
# se usa en obj mutables para saber si tienen la misma referencia
# y tmb para saber si una varible es True,False y None pq solo existe un obj de estos en todo el 
# programa osea que todos los obj True apuntan a la misma id
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True, porque tienen el mismo contenido
print(a is b)   # False, porque son listas distintas en memoria

x = True
y = True

print(x == y)   # True, mismo valor
print(x is y)   # True, misma identidad (es el mismo objeto)

x = None
y = None

print(x == y)   # True
print(x is y)   # True, ambos apuntan al único objeto None
