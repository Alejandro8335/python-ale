# funcion: la función que se aplicará a cada elemento.

# iterable: la colección de datos (lista, tupla, etc.) sobre la que se aplicará la función.


def multiplicar(x):
    return (x*x)
def sumar(x):
    return (x+x)

funcs = [multiplicar, sumar]
for i in range(5):
    valor = list(map(lambda x: x(i), funcs)) # lambda x: x(i) aplica la función x al número i
    print(valor)

# Salida:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]


############################################
# Como su nombre indica, filter crea una lista de elementos si usados en la llamada a una función devuelven True. 
# Es decir, filtra los elementos de una lista usando un determinado criterio
lista = range(-5, 5)
menor_cero = list(filter(lambda iter: iter < 0, lista))
print(menor_cero)

# Salida: [-5, -4, -3, -2, -1]
##############################################
# es muy útil cuando queremos realizar ciertas operaciones sobre una lista y devolver su resultado. 
from functools import reduce
producto = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Salida: 24