# ¿Qué es?
# -> deque (double-ended queue) es una clase del módulo collections en Python.
# -> Es una estructura de datos similar a una lista, pero optimizada para añadir
#    y quitar elementos tanto al principio como al final.
# -> Su nombre viene de "double-ended queue" (cola doblemente terminada).

from collections import deque

# ¿Para qué sirve?
# -> Sirve para manejar datos donde necesitamos eficiencia al insertar o eliminar
#    elementos en los extremos.
# -> Es más rápido que una lista cuando trabajamos con operaciones en los extremos.
# -> Se usa mucho en algoritmos de colas, pilas y estructuras circulares.

# Ejemplo básico: crear un deque
d = deque([1, 2, 3])
print(d)  # deque([1, 2, 3])

# ¿Cuándo se debe usar?
# -> Cuando necesitamos una cola (FIFO: primero en entrar, primero en salir).
# -> Cuando necesitamos una pila (LIFO: último en entrar, primero en salir).
# -> Cuando queremos trabajar con estructuras donde el acceso rápido a los extremos
#    es más importante que el acceso aleatorio.

# Métodos principales de deque:

# 1. append(x) -> agrega al final
d.append(4)
print(d)  # deque([1, 2, 3, 4])

# 2. appendleft(x) -> agrega al inicio
d.appendleft(0)
print(d)  # deque([0, 1, 2, 3, 4])

# 3. pop() -> elimina y devuelve el último
ultimo = d.pop()
print(ultimo, d)  # 4 deque([0, 1, 2, 3])

# 4. popleft() -> elimina y devuelve el primero
primero = d.popleft()
print(primero, d)  # 0 deque([1, 2, 3])

# 5. extend(iterable) -> agrega varios elementos al final
d.extend([4, 5])
print(d)  # deque([1, 2, 3, 4, 5])

# 6. extendleft(iterable) -> agrega varios elementos al inicio (en orden inverso)
d.extendleft([-1, -2])
print(d)  # deque([-2, -1, 1, 2, 3, 4, 5])

# 7. rotate(n) -> rota los elementos n pasos a la derecha (si n es negativo, a la izquierda)
d.rotate(2)
print(d)  # deque([4, 5, -2, -1, 1, 2, 3])

# 8. clear() -> elimina todos los elementos
d.clear()
print(d)  # deque([])


# Profundización: maxlen en deque
# -------------------------------
# ¿Qué es?
# -> maxlen es un parámetro opcional que podemos pasar al crear un deque.
# -> Define la capacidad máxima (el número máximo de elementos que puede contener).
# -> Si el deque ya está lleno y agregamos un nuevo elemento, automáticamente
#    se elimina el más antiguo del otro extremo.

# ¿Para qué sirve?
# -> Sirve para crear estructuras de datos con tamaño fijo.
# -> Es útil en buffers circulares, historial limitado, o cuando queremos
#    mantener solo los últimos N elementos.

# Ejemplo: crear un deque con maxlen=5
d = deque(maxlen=5)

# Agregamos elementos
for i in range(1, 7):  # agregamos 6 elementos
    d.append(i)
    print(d)

# Resultado paso a paso:
# 1 -> deque([1])
# 2 -> deque([1, 2])
# 3 -> deque([1, 2, 3])
# 4 -> deque([1, 2, 3, 4])
# 5 -> deque([1, 2, 3, 4, 5])  # lleno
# 6 -> deque([2, 3, 4, 5, 6])  # al agregar 6, se elimina el más antiguo (1)

# ¿Cuándo se debe usar?
# -> Cuando necesitamos mantener un historial limitado (ejemplo: últimos 10 movimientos).
# -> Cuando queremos un buffer circular que se actualice automáticamente.
# -> Cuando no queremos preocuparnos por eliminar manualmente elementos viejos.

# Ejemplo práctico: historial de últimas acciones
acciones = deque(maxlen=3)
acciones.append("login")
acciones.append("ver perfil")
acciones.append("editar perfil")
print(acciones)  # deque(['login', 'ver perfil', 'editar perfil'], maxlen=3)

acciones.append("logout")  # al agregar una nueva acción, se elimina la más antigua
print(acciones)  # deque(['ver perfil', 'editar perfil', 'logout'], maxlen=3)