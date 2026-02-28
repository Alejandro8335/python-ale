# ¿Qué es?
# -> namedtuple es una función del módulo collections en Python.
# -> Crea una clase especial de tuplas con nombre para cada campo.
# -> Es como una tupla normal, pero podemos acceder a los elementos por nombre
#    además de por índice.

from collections import namedtuple

# ¿Para qué sirve?
# -> Sirve para crear estructuras de datos ligeras y legibles.
# -> Nos permite agrupar datos relacionados sin tener que usar clases completas.
# -> Hace que el código sea más claro porque accedemos a los valores con nombres.

# Ejemplo básico: crear un namedtuple para representar un Punto en 2D
Punto = namedtuple("Punto", ["x", "y"])
p = Punto(3, 4)

print(p)        # Punto(x=3, y=4)
print(p.x)      # 3 (acceso por nombre)
print(p[1])     # 4 (acceso por índice)



# Pregunta: ¿Por qué es necesario el primer string "Punto"
# si ya estamos guardando la clase en una variable llamada Punto?

# Respuesta:
# -> El primer string NO es redundante, cumple un rol distinto al nombre de la variable.
# -> Ese string define el **nombre interno de la clase** que se crea.
# -> La variable en la que lo guardamos es solo una referencia en nuestro código.
# -> Aunque la variable se llame igual, el string es lo que Python usa para:
#    - Mostrar el nombre en la representación (repr/print).
#    - Identificar la clase en el sistema de tipos.
#    - Dar claridad cuando imprimimos objetos.

# Ejemplo:
Punto = namedtuple("Punto", ["x", "y"])
p = Punto(3, 4)

print(p)        # Punto(x=3, y=4) -> el nombre "Punto" viene del string, no de la variable
print(type(p))  # <class '__main__.Punto'> -> la clase realmente se llama "Punto"

# Si usamos otro nombre en el string:
Coordenada = namedtuple("Punto", ["x", "y"])  # variable se llama Coordenada, clase se llama "Punto"
c = Coordenada(5, 6)

print(c)        # Punto(x=5, y=6) -> se imprime "Punto" porque ese fue el nombre dado en el string
print(type(c))  # <class '__main__.Punto'> -> la clase creada se llama "Punto"

# Conclusión:
# - La variable (Punto, Coordenada, etc.) es solo cómo accedemos a la clase en nuestro código.
# - El string define el nombre oficial de la clase creada.
# - Por eso es necesario: sin ese string, la clase no tendría un nombre legible.



# ¿Cuándo se debe usar?
# -> Cuando necesitamos una estructura simple para agrupar datos.
# -> Cuando queremos algo más legible que una tupla normal.
# -> Cuando no necesitamos toda la funcionalidad de una clase.

# Métodos y características útiles de namedtuple:

# 1. _fields -> devuelve los nombres de los campos
print(Punto._fields)  # ('x', 'y')

# 2. _replace(**kwargs) -> crea una copia con algunos valores cambiados
p2 = p._replace(y=10)
print(p2)  # Punto(x=3, y=10)

# 3. _asdict() -> convierte el namedtuple en un diccionario
print(p._asdict())  # {'x': 3, 'y': 4}

# 4. Se comporta como una tupla normal en iteraciones
for valor in p:
    print(valor)  # imprime 3 y 4

# Ejemplo práctico: representar una persona
Persona = namedtuple("Persona", ["nombre", "edad", "ciudad"])
alejandro = Persona("Alejandro", 25, "Rosario")
print(alejandro.nombre, alejandro.edad, alejandro.ciudad)
# Resultado: Alejandro 25 Rosario