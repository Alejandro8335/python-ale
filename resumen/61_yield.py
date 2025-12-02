# ¿Qué es yield?
# yield es una palabra clave que convierte una función en un generador.

# Un generador es como una función que se puede pausar y reanudar.

# En vez de devolver un valor y terminar (como con return), 
# yield devuelve un valor pero deja la función "congelada" en ese punto, 
# lista para continuar después.

def contador():
    yield 1
    yield 2
    yield 3

gen = contador()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

# Cada vez que llamas next(gen), la función avanza hasta el siguiente yield.

# Cuando ya no hay más valores, lanza StopIteration.

def cuadrados(n):
    for i in range(n):
        yield i * i

for valor in cuadrados(5):
    print(valor)
# 0
# 1
# 4
# 9
# 16
# return → termina la función y devuelve un único valor.
# yield → puede devolver muchos valores, uno por uno, sin perder el estado interno.