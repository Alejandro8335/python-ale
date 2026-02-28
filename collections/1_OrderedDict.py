# ¿Qué es?
# -> OrderedDict es una clase del módulo collections en Python.
# -> Es un diccionario que recuerda el orden en el que se agregan las claves.
# -> En versiones modernas de Python (>=3.7), los diccionarios normales también
#    mantienen el orden de inserción, pero OrderedDict ofrece métodos extra.

from collections import OrderedDict

# ¿Para qué sirve?
# -> Sirve para trabajar con diccionarios donde el orden de las claves importa.
# -> Permite operaciones especiales como "move_to_end" para reorganizar claves.
# -> Es útil cuando necesitamos estructuras que dependan del orden de inserción
#    o cuando queremos dejar claro que el orden es relevante.

# Ejemplo: crear un OrderedDict
mi_diccionario = OrderedDict()
mi_diccionario["a"] = 1
mi_diccionario["b"] = 2
mi_diccionario["c"] = 3

print(mi_diccionario)
# Resultado: OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Ejemplo de método especial: mover una clave al final
mi_diccionario.move_to_end("b")
print(mi_diccionario)
# Resultado: OrderedDict([('a', 1), ('c', 3), ('b', 2)])

# ¿Cuándo se debe usar?
# -> Cuando necesitamos manipular el orden de las claves explícitamente.
# -> Cuando queremos dejar claro en el código que el orden de inserción es importante.
# -> Aunque los dict normales ya mantienen orden, OrderedDict sigue siendo útil
#    por sus métodos adicionales y su semántica más explícita.
