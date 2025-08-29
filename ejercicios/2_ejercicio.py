#falto el profe y los pibes van a armar la clase

#pedir el nombre y la edad de los compañeros que venieron hoy a clases


def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []  
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        compañeros.append((nombre, edad))  
    compañeros.sort(key=lambda x: x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]

    return asistente, profesor

asistente, profesor = obtener_compañeros(5)

print(f"El asistente es: {asistente}")
print(f"El profesor es: {profesor}")