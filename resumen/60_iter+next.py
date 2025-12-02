# Convierte un objeto iterable (lista, tupla, string, diccionario, etc.) en un iterador.
iterador = iter([1, 2, 3])

# next
# Avanza un iterador y devuelve el siguiente elemento.
valor = next(iterador)
print(valor)
# Cuando ya no quedan elementos, lanza StopIteration.

##############
lista = [10, 20, 30]
it = iter(lista)

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
try:
    print(next(it))  # StopIteration (error)
except StopIteration:
    print("StopIteration")
# El StopIteration no es un error “grave”, 
# es simplemente la forma en que Python avisa que ya no hay más elementos.
##############
# Un for en Python usa internamente iter y next.
it = iter([10, 20, 30])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break

##############  
# iter(obj) → crea un iterador a partir de un iterable.

# next(it) → obtiene el siguiente valor del iterador.

# Cuando no hay más valores → StopIteration.

# Los bucles for ya usan iter y next por debajo, 
# por eso casi nunca necesitas llamarlos manualmente, salvo que quieras control fino.