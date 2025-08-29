
#forma no optima de sumar valores
#def suma(lista):
#    for numero in lista:
#       numero_sumados = numero_sumados + numero
#    return numero_sumados

#resultado = suma([5,3,9])
#print(resultado)

#forma optima,utilizando el parametro *args

def suma(*numeros):
    return sum(numeros)
    
resultado = suma(5,3,9)
print(resultado)

#forma de sumar valores
def suma2(numeros2):
    return sum([*numeros2])

resultado2 = suma2([5,3,9])
print(resultado2)