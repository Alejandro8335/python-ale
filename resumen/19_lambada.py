# ¿Qué son las funciones lambda?
# Son funciones anónimas (sin nombre) que se definen en una sola línea.

# Se usan para operaciones rápidas y simples, donde no vale la pena escribir una función completa con def.

###############################################################

# Sintaxis
# lambda argumentos: expresión
# argumentos → los parámetros que recibe la función.

# expresión → lo que devuelve (siempre una sola expresión).

############################################################### 
# Se integran bien con funciones de orden superior (map, filter, sorted, etc.).

###############################################################
cuadrado_lambda = lambda x: x * x

print(cuadrado_lambda(5))  # 25
print(cuadrado_lambda(10))  # 100

################################################################
# Los argumentos son las variables de entrada.

# La expresión es una fórmula que usa esos argumentos y devuelve un resultado.

# Siempre es una sola expresión (no se pueden poner varias sentencias, bucles, ni if largos).
# Aunque sí se puede usar un if corto en forma de expresión:

operacion = lambda x, y, z: (x + y) * z
print(operacion(2, 3, 4))  # (2+3)*4 = 20


par_o_impar = lambda x: "par" if x % 2 == 0 else "impar"
print(par_o_impar(3))  # "impar"
##################################################################
# Con def: siempre se crea un nombre en el namespace.

# Con lambda: solo aparece en el namespace si la asignas a una variable; 
# si no, es una función “anónima” que vive en memoria mientras se usa.