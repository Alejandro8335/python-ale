diccionario = {
    "nombre" : "ale",
    "apellido": "dominguez" ,
    "edad" : "15"
}
#devuelve todas las claves
claves = diccionario . keys()

#devuelve el elemento
valor = diccionario.get("nombre")#si no ensuentra nada devuelve none

valor_2 = diccionario["nombre"]#si no ensuentra nada devuelve error

#eliminando todo del diccionario
# diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("edad")

#obteniendo un elemento iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)