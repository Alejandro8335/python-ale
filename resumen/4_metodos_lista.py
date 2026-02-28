#creando una lista con list()
lista =list(("hola","ale",15))

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista 
lista.append("nuevo")

#agregando un elemento a la lista en un indice en especifico
print(lista)
lista.insert(2,"nuevo2")
print(lista)
#agregando varios elementos a la lista 
lista.extend((False,2020))

#eliminando un elemento de la lista (por su indice)
lista.pop(0)
#-1 se elimina el ultimo elemento y asi sucesivamente

#revuele un elemento de la lista por su valor 
lista.remove("nuevo2")

#eliminando todo los elementos de la lista 
#lista.clear()

#ordenando la lista de forma acendente (si usamos el parametro reverse=true lo invierte)
#lista.sort()#solo funciona con numeros

#invirtiendo los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista 
elementos_encontrado = lista.index("ale")

a = [5, 4, 4]
b = a.copy()
b[0] = 99
print(a)  # Resultado: [5, 4, 4]
print(b)  # Resultado: [99, 4, 4]
print(id(a), id(b))

colores = ["rojo", "azul", "rojo", "verde", "rojo"]
resultado = colores.count("rojo")   # Resultado: 3
print(lista)


# Diferencia entre append y += en listas de Python
# ------------------------------------------------

bar = ["hola", "mundo"]

# 1. append()
# ¿Qué es?
# -> Agrega UN solo elemento al final de la lista.
# -> Ese elemento puede ser cualquier objeto: string, número, lista, etc.
# -> Siempre añade el objeto completo como una única entrada.

bar.append("adios")
print(bar)
# Resultado: ['hola', 'mundo', 'adios']

bar.append(["python", "listas"])
print(bar)
# Resultado: ['hola', 'mundo', 'adios', ['python', 'listas']]
# Nota: se agregó una lista como un solo elemento dentro de la lista principal.


# 2. += (concatenación)
# ¿Qué es?
# -> Une la lista original con otra lista.
# -> Agrega cada elemento de la lista de la derecha como elementos individuales.
# -> Es equivalente a usar extend().

bar = ["hola", "mundo"]
bar += ["adios"]
print(bar)
# Resultado: ['hola', 'mundo', 'adios']

bar += ["python", "listas"]
print(bar)
# Resultado: ['hola', 'mundo', 'adios', 'python', 'listas']
# Nota: aquí cada string se agregó como elemento separado, no como una lista dentro.


# Conclusión:
# - append(x) -> añade x como un único elemento al final.
# - += [x, y] -> añade cada elemento de la lista a la lista original.

# Ejemplo válido: concatenación con + 
lista1 = [1, 2] 
lista2 = [3, 4] 
print(lista1 + lista2) 
# Resultado: [1, 2, 3, 4] 

# Ejemplo válido: repetición con * 
lista = ["hola"] 
print(lista * 3) 
# Resultado: ['hola', 'hola', 'hola']