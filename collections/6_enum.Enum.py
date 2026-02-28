# ¿Qué es?
# -> Enum es una clase del módulo enum en Python.
# -> Sirve para crear enumeraciones: conjuntos de valores constantes con nombre.
# -> Cada miembro de la enumeración es único e inmutable.

from enum import Enum

# ¿Para qué sirve?
# -> Sirve para representar valores fijos y predefinidos de manera clara.
# -> Evita el uso de "magic numbers" o strings sueltos en el código.
# -> Hace que el código sea más legible y menos propenso a errores.

# Ejemplo básico: definir una enumeración de colores
class Color(Enum):
    ROJO = 1    # -> Los números no son lo más importante, son solo "valores asociados".
    VERDE = 2
    AZUL = 3

print(Color.ROJO)       # Color.ROJO
print(Color.ROJO.value) # 1
print(Color.ROJO.name)  # 'ROJO'

# ¿Cuándo se debe usar?
# -> Cuando tenemos un conjunto limitado de opciones posibles.
# -> Ejemplo: estados de un proceso, días de la semana, roles de usuario.
# -> Cuando queremos que esas opciones sean constantes y no se modifiquen.

# Ejemplo práctico: estados de un semáforo
class Semaforo(Enum):
    ROJO = "Detener"
    AMARILLO = "Precaución"
    VERDE = "Avanzar"

estado = Semaforo.ROJO
print(estado.value)  # "Detener"

# Métodos y características útiles de Enum:

# 1. Iterar sobre los miembros
for color in Color:
    print(color)
# Resultado:
# Color.ROJO
# Color.VERDE
# Color.AZUL

# 2. Comparación
print(Color.ROJO == Color.VERDE)  # False
print(Color.ROJO == Color.ROJO)   # True

# 3. Acceso por nombre
print(Color["AZUL"])  # Color.AZUL

# 4. Acceso por valor
print(Color(2))  # Color.VERDE

# Nota:
# -> Los valores de Enum son únicos, no se pueden cambiar ni reasignar.
# -> Esto garantiza consistencia en el código.
