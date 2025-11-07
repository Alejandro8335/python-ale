# Es un operador de pertenencia.
# Sirve para comprobar si un elemento está contenido dentro de una secuencia
# (string, lista, tupla, diccionario, conjunto).

# Con cadenas
print("a" in "casa")      # True, porque "a" aparece en "casa"
print("z" in "casa")      # False, porque "z" no está

# Con listas
print(3 in [1, 2, 3, 4])  # True
print(5 in [1, 2, 3, 4])  # False

# Con tuplas
print("rojo" in ("rojo", "verde", "azul"))  # True

# Con diccionarios
d = {"a": 1, "b": 2}
print("a" in d)      # True (busca claves, no valores)
print(1 in d)        # False (porque 1 es un valor, no una clave)

# Con conjuntos
print(10 in {5, 10, 15})  # True