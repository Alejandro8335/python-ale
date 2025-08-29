#abrimos el archivo
archivo = open("C:/Users/gabri/OneDrive/Desktop/ALE/python=ale/ale.txt")
#print(archivo.read())                                             

#leer linea por linea
#linea_1 = archivo.readlines()

#leer una solo linea
linea_1 = archivo.readline() #podemos decirle cuanta cantidad de caracteres queremos que lea
print(linea_1)

#cerrar el archivo
archivo.close()