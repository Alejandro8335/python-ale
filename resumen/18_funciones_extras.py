
#creando unafuncion de tres parametros 
def frase(nombre,apellido,adjetivo):
    return f"hola {nombre} {apellido}, sos muy {adjetivo}"

#utilizando keyword argumentos
frase_resultante = frase(adjetivo = "capo",nombre = "ale",apellido = "dominguez")
print(frase_resultante)

#creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo = "tonto"):
    return f"hola {nombre} {apellido}, sos muy {adjetivo}"

frase_resultante2 = frase("ale","dominguez","inteligente")
print(frase_resultante2)