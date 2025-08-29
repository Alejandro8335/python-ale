nombre = "hola Ale"
nombre2="chau"
numero= "45,6,8,9"
#convierte todo en mayuscula
mayusc=nombre.upper()

#convierte a minusculas
minusc=nombre.lower()

#primera letra mayuscula 
primer_letra_mayusc= nombre.capitalize()

#buscamos una cadena en otra cadena
busqueda_find= nombre.find("hola")
#devueve las cordenadas de la palabra, sino encuentra nada devuelve -1

#buscamos una cadena en otra cadena 
busqueda_index = nombre2.index("c")

#si es numerico devuelve true,si no falso
es_numerico= numero.isnumeric()

#si es un alfanumerico devovemos true,sino falso 
es_alfanumerico = numero.isalpha()
#solo cuenta letras de la A a la Z

#buscamos en una cadena en otra cadena,devuelve la cantidad de veces que coincida
contar_concidencias = nombre.count("l")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = nombre.__len__()
contar_caracteres2 = len(nombre)

#verificamos si una cadena empieza con otra cadena dada,si es asi devuelve true
empieza_con = nombre.startswith("hola")

#verificamos si una cadena termina con otra cadena dada,si es asi devuelve true
termina_con = nombre.endswith("Ale")

#remplaza un pedazo de cadena dada,por otra dada
cadena_nueva = numero.replace("5","7")

#separar cadenas con la cadena que le pasemos(hace una lista)
cadena_separada = numero.split(",")

print(cadena_separada)

cadena = "0123456789"
print(cadena[2:7])