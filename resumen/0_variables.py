#VARIABLES
#una variable es un nombre que almacena un valor.

#tipos de datos / tipos de variables:
#str(cadenas de texto)
#int(numeros)
#float(numeros con coma/numeros con distintas propiedades)
#bool(booleanos(True/False))
#print(type())

#concatenar con +
nombre = "ale"
bienbenida = "hola "+nombre+"¿como estas?"

#f stream (combierte todo a texto)
bienvenida = f"hola {nombre} ¿como estas?"

#del (borra datos)
#operadores de pertenecia(in/not in)
print("6" in bienvenida)#false

#variable con snake_case
nombre_completo = "alejandro dominguez"

#DATOS COMPUESTOS
#list
lista=["ale","soy ale",15]
#se cuenta del 0 al 9
print(lista[0])#ale

#tupla (no se pueden modificar)
tupla=("ale","soy ale",15)

#conjonto(sed)
conjunto ={"ale","soy ale",15}
#se puedes redefinirlo pero no podes modificar los elementos.no permite repetir valores.no podes 
#acceder un elemento por indice
#print(conjunto[3])=error

#diccionario(dict)
dicionario={
    "nombre":"ale",
    'nombre_completo':"alejandro dominguez",
    "edad":15
}
#termino:clave,valor
print(dicionario["edad"])#15
#print(dicionario[1])error
