
numeros = {1,2,3,4,5}

#encontrando el numero mayor de una lista
nemuro_max = max(numeros)
print(f"0 {nemuro_max}")

#encontrando el numero menor de una lista
nemuro_min = min(numeros)
print(f"1 {nemuro_min}")

#redondiando a 6 decimales(o mas)
numero = round(12.12345678,8)
print(numero)

#retorna false -> 0,vacio,false o ninguno / true -> distinto a 0,true,cadena
resultado = bool(1)
print(resultado)

#retorna true,si todos los valores son verdaderos 
resultado_2 = all([234,True,"HOLA"])
print(resultado_2)

#suma todos los valores de un iterable 
suma_total = sum(numeros)
print(suma_total)