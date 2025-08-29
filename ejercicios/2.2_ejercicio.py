#creando una funcion que nos devuelva loa numeros primos
#entre el 0 argunmento que pasamos

#crear una funcion que verifique si un numero es primo 
def es_primos(num):
    for i in range(2,num-1):
        if num %i==0 : return False
    return True

def primos_asta(num):
    primos = []
    for i in range(3,num+1):
        resultado = es_primos (i)
        if resultado == True: primos.append(i)
    return primos
resultado = primos_asta(7)
print(resultado)