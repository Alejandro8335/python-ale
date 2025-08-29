
def decorador(funcion):
    def modificada():
        print("antes de llamar a la función")
        funcion()
        print("después")
    return modificada

# def saludo():
#     print("hola mundo")

# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
    print("hola mundo")
    
saludo()