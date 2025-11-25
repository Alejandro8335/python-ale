#creando una lista con list()
lista =list(("hola","ale",15))

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista 
lista.append("nuevo","hola")

#agregando un elemento a la lista en un indice en especifico
lista.insert(2,"nuevo2")

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

print(lista)