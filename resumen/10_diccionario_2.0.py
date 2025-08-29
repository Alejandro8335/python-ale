
#creando diccionario con dict()
diccionario = dict(nombre = "ale",apellido = "dominguez")

#las lista no pueden ser claves y usamos frozenset para meter conjuntos
diccionario1 = {frozenset(["ale","hola"]):"JAJAJJA"}

#creando diccionario con fromkeys:valor por defecto none
diccionario2 = dict.fromkeys(["nombre","apellido"])

#creando diccionario con fromkeys() cambiando el valor por defecto a "ale"
diccionario3 = dict.fromkeys(["nombre","apellido"],"ale")


print(diccionario3)