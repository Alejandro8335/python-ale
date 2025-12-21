diccionario ={
    "nombre" : "ale",
    "apellido": "dominguez",
    "edad" : 15
}     

#recoriendo un diccionario para obtener la clave 
for key in diccionario:
    print(f"la clave es: {key}")
    
    
#recoriendo un diccionario con items() para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")
    
diccionario_nombres_edad = {}
for nombres, edad in [("ale",15),("facha",20),("pana",25)]:
    diccionario_nombres_edad[nombres] = edad
print(diccionario_nombres_edad)