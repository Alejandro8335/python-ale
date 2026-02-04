# El slicing permite extraer porciones de secuencias (listas, tuplas, cadenas) 
# usando la sintaxis secuencia[inicio:fin:paso], donde inicio se incluye, 
# fin no se incluye, y paso es opcional para el salto entre elementos

#######################################################

# secuencia[inicio:fin:paso]

# inicio: índice donde comienza (incluido).

# fin: índice donde termina (no incluido).

# paso: salto entre elementos (opcional). Esta sintaxis es la forma 
# estándar para crear cortes en Python

#######################################################
a = [0,1,2,3,4,5]
print(a[1:4])   # [1,2,3]

a[:3]    # desde inicio hasta índice 2
a[3:]    # desde índice 3 hasta el final
a[:]     # copia completa de la secuencia

a[::2]   # elementos con paso 2 -> [0,2,4]
a[::-1]  # invierte la secuencia -> [5,4,3,2,1,0]

#######################################################
# |
s = slice(1, 5, 2)
a[s]     # equivalente a a[1:5:2]