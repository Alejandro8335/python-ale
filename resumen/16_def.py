
#creando una funcion simple
def saludar():
    print("hola")

#ejecutando una funcion siemple
saludar()
saludar()

#creando una funcion que tenga parametros
def saludar(nombre,sexo): 
    sexo = sexo.lower()
    if(sexo =="mujer"):
        adjetivo = "mi reina"
    elif(sexo == "hombre"):
        adjetivo ="maestro"
    else:
        adjetivo = "crack"
    
    print(f"hola {nombre}, {adjetivo}")

saludar("ale","HOmbre")

#creando una funcion que nos retorne valores 
def contraseña1(num):
    listado= "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{listado[c1]}{listado[c2]}{listado[c3]}{num*2}"
    return contraseña,num
    
#desempaquetando la funcion
password,numero = contraseña1(1)

#mostrando el resultado obtenido y los datos utilizados para obtenerlo
print(f"tu contraseña es: {password}")
print(f"el numero utilizado es: {numero}")


