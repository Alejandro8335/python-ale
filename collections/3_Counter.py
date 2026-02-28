# ¿Qué es?
# -> Counter es una clase del módulo collections en Python.
# -> Es un tipo especial de diccionario diseñado para contar elementos.
# -> Cada clave representa un objeto y su valor es la cantidad de veces que aparece.

from collections import Counter

# ¿Para qué sirve?
# -> Sirve para contar ocurrencias de elementos en listas, strings u otros iterables.
# -> Nos evita tener que escribir bucles manuales para contar.
# -> Es muy útil en análisis de datos, procesamiento de texto y estadísticas rápidas.

# Ejemplo básico: contar letras en una palabra
conteo = Counter("banana")
print(conteo)
# Resultado: Counter({'a': 3, 'n': 2, 'b': 1})

# Ejemplo con lista: contar frutas
frutas = ["manzana", "pera", "manzana", "banana", "pera", "manzana"]
conteo_frutas = Counter(frutas)
print(conteo_frutas)
# Resultado: Counter({'manzana': 3, 'pera': 2, 'banana': 1})

# ¿Cuándo se debe usar?
# -> Cuando necesitamos saber cuántas veces aparece cada elemento.
# -> Cuando queremos obtener los elementos más comunes rápidamente.
# -> Cuando trabajamos con datos repetidos y necesitamos estadísticas simples.

# Métodos útiles de Counter:

# 1. most_common(n)
# Devuelve los n elementos más frecuentes.
print(conteo_frutas.most_common(2))
# Resultado: [('manzana', 3), ('pera', 2)]

# 2. elements()
# Devuelve un iterador con todos los elementos repetidos según su conteo.
print(list(conteo_frutas.elements()))
# Resultado: ['manzana', 'manzana', 'manzana', 'pera', 'pera', 'banana']

# 3. update(iterable)
# Actualiza el conteo con nuevos elementos.
conteo_frutas.update(["banana", "banana"])
print(conteo_frutas)
# Resultado: Counter({'manzana': 3, 'banana': 3, 'pera': 2})

# 4. subtract(iterable)
# Resta ocurrencias de los elementos.
conteo_frutas.subtract(["manzana", "banana"])
print(conteo_frutas)
# Resultado: Counter({'manzana': 2, 'banana': 2, 'pera': 2})



# Operaciones matemáticas entre Counter
# -------------------------------------

# 1. Suma (+)
# ¿Qué es? -> Combina dos contadores sumando las ocurrencias de cada clave.
# ¿Para qué sirve? -> Para unir conteos de diferentes fuentes.
# ¿Cuándo usarlo? -> Cuando queremos obtener un conteo total de varios conjuntos.

c1 = Counter(a=2, b=3)
c2 = Counter(a=1, b=1, c=2)
print(c1 + c2)
# Resultado: Counter({'b': 4, 'a': 3, 'c': 2})


# 2. Resta (-)
# ¿Qué es? -> Resta las ocurrencias de un contador respecto a otro.
# ¿Para qué sirve? -> Para eliminar o descontar elementos de un conteo.
# ¿Cuándo usarlo? -> Cuando queremos saber qué queda después de quitar elementos.

print(c1 - c2)
# Resultado: Counter({'b': 2, 'a': 1})
# Nota: las claves con valores <= 0 se eliminan automáticamente.


c1 = Counter(a=2, b=3)        # 'a' aparece 2 veces, 'b' aparece 3 veces
c2 = Counter(a=1, b=1, c=2)   # 'a' aparece 1 vez, 'b' aparece 1 vez, 'c' aparece 2 veces


# 3. Intersección (&)
# -------------------------------------------------
# ¿Qué es?
# -> Toma las claves que están en ambos contadores y se queda con el MÍNIMO valor de cada una.
# -> Es como decir: "¿Cuál es la cantidad mínima que comparten en común?"

print(c1 & c2)
# Resultado: Counter({'a': 1, 'b': 1})
# Explicación:
# - 'a' está en ambos: c1 tiene 2, c2 tiene 1 -> mínimo = 1
# - 'b' está en ambos: c1 tiene 3, c2 tiene 1 -> mínimo = 1
# - 'c' no está en c1, así que no aparece en la intersección.


# 4. Unión (|)
# -------------------------------------------------
# ¿Qué es?
# -> Toma todas las claves que aparecen en cualquiera de los contadores y se queda con el MÁXIMO valor de cada una.
# -> Es como decir: "¿Cuál es la cantidad máxima registrada en cualquiera de los dos?"

print(c1 | c2)
# Resultado: Counter({'b': 3, 'a': 2, 'c': 2})
# Explicación:
# - 'a' está en ambos: c1 tiene 2, c2 tiene 1 -> máximo = 2
# - 'b' está en ambos: c1 tiene 3, c2 tiene 1 -> máximo = 3
# - 'c' solo está en c2 con valor 2 -> se incluye con 2

# En resumen:
# - Intersección (&) -> se queda con lo mínimo compartido.
# - Unión (|) -> se queda con lo máximo encontrado.
