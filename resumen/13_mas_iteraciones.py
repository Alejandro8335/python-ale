
frutas = ["bananas","manzana","ciruela","pera","naranja"]

#evitando que se ejecute una variable con la setencia continue
for fruta in frutas :
    if fruta == "ciruela":
        continue
    print(f"me voy a comer una {fruta}")

#evitando que el siga ejecutandose(el else no se ejecuta tampoco)
for fruta in frutas :
    if fruta == "naranja":
        break
    print(f"1me voy a comer una {fruta}")

#tambien se puede poner al reves y que termine destues de print
for fruta in frutas :
    print(f"2me voy a comer una {fruta}")
    if fruta == "pera":
        break

#recorer una cadena de texto
cadena = "hola ale"

for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo
numeros = [2,4,6,8,10]
numeros_dumtiplicados =[x*2 for x in numeros]#no necesariamente tiene que ser x
print(numeros_dumtiplicados)

