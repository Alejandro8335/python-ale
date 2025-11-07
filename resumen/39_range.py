#range(inicio, fin, paso)

# inicio → El número desde donde empieza la secuencia (incluido).
# Si no lo pones, por defecto es 0.

# fin → El número donde termina la secuencia (excluido).
# La secuencia se detiene antes de llegar a este valor.

# paso → El incremento o decremento entre cada número.
# Si no lo pones, por defecto es 1.
# Puede ser negativo para contar hacia atrás.

#CUIDADO,1 valor es el fin; 2 valores es inicio y fin; y 3 valores es inicio,fin y paso

# Ejemplo 1: Solo fin
for i in range(5):
    print(i) 
# Salida: 0, 1, 2, 3, 4

# Ejemplo 2: inicio y fin
for i in range(2, 7):
    print(i)
# Salida: 2, 3, 4, 5, 6

# Ejemplo 3: inicio, fin y paso
for i in range(1, 10, 2):
    print(i)
# Salida: 1, 3, 5, 7, 9

# Ejemplo 4: paso negativo (cuenta regresiva)
for i in range(10, 0, -2):
    print(i)
# Salida: 10, 8, 6, 4, 2
