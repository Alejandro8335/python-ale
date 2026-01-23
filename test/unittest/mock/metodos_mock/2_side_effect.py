# Se usa para definir qué pasa cuando se llama al mock:

# Simular excepciones → el mock lanza un error en lugar de devolver algo.

# Secuencia de valores → el mock devuelve distintos resultados en cada llamada.

# Función personalizada → el mock ejecuta una función que tú defines.

from unittest.mock import Mock

m = Mock()
m.obtener.side_effect = ValueError("Error simulado")

try:
    m.obtener()
except ValueError as e:
    print(e)   # → "Error simulado"

############################################################################

m = Mock()
m.calcular.side_effect = [1, 2, 3]

print(m.calcular())  # → 1
print(m.calcular())  # → 2
print(m.calcular())  # → 3

############################################################################

def doble(x):
    return x * 2

m = Mock()
m.procesar.side_effect = doble

print(m.procesar(5))   # → 10
print(m.procesar(7))   # → 14