
animales = ["gato","perro","loro","cocodrilo"]

#recorriendo la lista animales
for animal in animales: 
    print(animal)

#recorriendo la lista y multiplicando cada valor por 10
numeros = [1,2,3,4]
for numero in numeros:
    resultado = numero *2
    print(resultado)
    
#iterando dos listas del mismo tamaño al mismo tiempo(no es necesario que sean del mismo tamaño, se detiene en la mas corta) 
for numero,animal in zip(numeros,animales):
    print(f"recoriendo lista 1: {numero}")
    print(f"recoriendo lista 2: {animal}")
    
#para combinar mas de dos listas se usa zip
    
#forma no optima de recorer un lista(no funciona en conjuntos/set)
for numero in range(len(numeros)):
    print(numeros[numero])
    
#forma correcta de recorrer una lista con su indice
for numero in enumerate(numeros):
    indice = numero[0]
    valor = numero[1]
    print(f"el indice es: {indice} y el valor es: {valor}")

for indice,valor in enumerate(numeros):
    print(f"el indice es: {indice} y el valor es: {valor}")
    
#sirve para recorrer una lista (o cualquier iterable) y obtener tanto el índice como el valor    
    
#usando el for else 
for numero in numeros:
    print(f"valor actual: {numero}")
else:
    print("fin")#siempre se muestra pero al final del bucle

#funciona igual para tuplas que para listas y set(pero con algunas diferencias)


# reversed() sirve para iterar sobre una secuencia en orden inverso.
for i in reversed(range(5)):
    print(i)
    
# con range se puede mejor pero es solo un ejemplo
for i in range(4,-1,-1): # va desde 4 hasta 0
    print(i)
    

for i in range(5):
    if i == 3:break
else:# se ejecuta si no hay ningun break
    print("no se ejecuta")