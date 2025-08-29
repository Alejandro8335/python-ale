
import re

texto = '''hola maaaestro,esta es la cadena 1. como estas mi capitan?
esta es la linea 2772277 de texto
esta es la linea 2 de texto
y esta es la final(linea 3) definitiva mi cacapitan...'''

#search para buscar una sola concidencia
resultado = re.search("hola",texto)

#haciendop una busqueda simple
resultado1 = re.findall("esta",texto,flags=re.IGNORECASE)
#flags=re.IGNORECASE:ignora las mayusculas

#\d -> busca digitos numericos del 0-9
resultado2 = re.findall(r"\d",texto)
#con la r le decimos que es posible que usemos expreciones regulares

#\D -> busca TODO MENOS  digitos numericos del 0-9
resultado3 = re.findall(r"\D",texto)

#\w -> busca caracteres alfanumericos [a-z,A-Z,0-9,_]
resultado4 = re.findall(r"\w",texto)

#\W -> busca TODO MENOS caracteres alfanumericos [a-z,A-Z,0-9,_]
resultado5 = re.findall(r"\W",texto)
#nos muestra ( (espacios)),(,(coma)) y (\n(espacios en linea))

#\s -> busca espacios en linea -> espacios,tabs,saltos de linea
resultado6 = re.findall(r"\s",texto)

#\S -> busca TODO MENOS espacios en linea -> espacios,tabs,saltos de linea
resultado7 = re.findall(r"\S",texto)

#(.) -> busca TODO MENOS saltos de linea
resultado8 = re.findall(r".",texto)

#\n -> busca saltos de linea
resultado9 = re.findall(r"\n",texto)

#\ -> cancela caracteres especiales,cancelando la funcion del (.) y buscando (.)
resultado10 = re.findall(r"\.",texto)
   
#armando una cadena que busque un numero,seguido de un punto y un espacio
resultado11 = re.findall(r"\d\.\s",texto)  

#^ -> busca el comienzo de una linea
resultado12 = re.findall(r"^hola",texto)#nos devuelve la palabra
#busca si la palabra esta al comienzo del str

#flags=r.m -> activa la multilinea
resultado13 = re.findall(r"^esta",texto,flags= re.M)

#$ -> busca el final de una linea
resultado14 = re.findall(r"texto$",texto,flags= re.M)

#{n} -> busca n cantidad de veces al valor de la izquierda
resultado15 = re.findall(r"\d{3}",texto)

#{n,m} -> al menos n,com maximo m
resultado16 = re.findall(r"\d{2,4}",texto)

resultado17 = re.findall(r"ma{2,4}",texto)#m+a{2,4}

resultado18 = re.findall(r"(ca){2}",texto)#devuelve "ca"  /  ((?:ca)) para que devuelva "caca "
#nos devuelve "ca"  cada vez que encuentra "caca"

resultado19 = re.findall(r"[ca]{2}",texto)#nos devuelve cualquiera de estos valores:"aa","ac","ca" y "cc"

# | -> busca una cosa o la otra(propiedad/condicion o)
resultado20 = re.findall(r"\d{2,4}|hola",texto)#nos lo devuelve en el orden de la cadena

# re.sub(patrón, reemplazo, texto, conteo)
# patrón: La expresión regular a buscar en el texto.
# reemplazo: El texto que sustituirá las coincidencias.
# texto: La cadena donde se hará la búsqueda y sustitución.
# conteo (opcional): Número máximo de reemplazos. Si no se especifica, reemplaza todas las coincidencias.
print(resultado20)