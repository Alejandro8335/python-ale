
#creando una funcion lambda para multiplicar por dos
multiplicar_xdos = lambda x : x*2

print(multiplicar_xdos(5))

#creando una funcion comun que duga si es par o no
def es_par(num):
    if(num%2==0):
        return True
    
#usando filter con uns funcion comun 
numeros = [1,2,3,4,5,6,7,8,9]
numeros_pares = filter(es_par,numeros)

print(list(numeros_pares))

#creando lo mismo que antes pero con lambda
numeros_pares2 = filter(lambda numero:numero%2 ==1,numeros)
print(list(numeros_pares2))

#Son funciones anónimas, de una sola expresión,
#útiles cuando necesitas definir un comportamiento rápido sin nombrarlo.