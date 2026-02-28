# ¿Qué es?
# -> defaultdict es una clase del módulo collections en Python.
# -> Es como un diccionario normal, pero con una diferencia clave:
#    si intentamos acceder a una clave que no existe, en lugar de dar error,
#    crea automáticamente un valor por defecto.

from collections import defaultdict

# ¿Para qué sirve?
# -> Sirve para evitar errores al acceder a claves inexistentes.
# -> Nos permite definir un "valor por defecto" para nuevas claves.
# -> Esto es útil cuando queremos agrupar datos o contar elementos sin tener que
#    comprobar si la clave ya existe.

# Ejemplo: crear un defaultdict con listas como valor por defecto
mi_diccionario = defaultdict(list)

mi_diccionario["frutas"].append("manzana")   # la clave "frutas" no existía, se crea con una lista vacía
mi_diccionario["frutas"].append("banana")

print(mi_diccionario)  
# Resultado: defaultdict(<class 'list'>, {'frutas': ['manzana', 'banana']})

# ¿Cuándo se debe usar?
# -> Cuando queremos trabajar con colecciones de datos y evitar escribir código extra
#    para inicializar claves.
# -> Ejemplo típico: agrupar elementos, contar ocurrencias, o crear estructuras
#    donde cada clave tiene un valor inicial automático.