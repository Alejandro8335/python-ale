
animales = ["gato","perro","loro","cocodrilo"]

#recorriendo la lista animales
for animal in animales: 
    print(animal)

#recorriendo la lista y multiplicando cada valor por 10
numeros =[1,2,3,4]
for numero in numeros:
    resultado = numero *2
    print(resultado)
    
#iterando dos listas del mismo tamaño al mismo tiempo 
for numero,animal in zip(numeros,animales):
    print(f"recoriendo lista 1: {numero}")
    print(f"recoriendo lista 2: {animal}")
    
#forma no optima de recorer un lista(no funciona en conjuntos/set)
for numero in range(len(numeros)):
    print(numeros[numero])
    
#forma correcta de recorrer una lista con su indice
for numero in enumerate(numeros):
    indice = numero[0]
    valor = numero[1]
    print(f"el indice es: {indice} y el valor es: {valor}")
    
#usando el for else 
for numero in numeros:
    print(f"valor actual: {numero}")
else:
    print("fin")#siempre se muestra pero al final del bucle

#funciona igual para tuplas que para listas y set(pero con algunas diferencias)
