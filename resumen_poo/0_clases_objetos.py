
#clases fijas
class Celular():
    marca = "samsung"
    modelo = "S23"
    camara = "48MP"
    #atributos

#objeto   
celular1 = Celular()

class celularr:
    def __init__(self,marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camaraa = camara
        
    #metodos
    def llamar(self):
        print(f"estas llamando desde un {self.modelo}")
    
    def cortar(self):
        print("termino la llamada")

#self(= a la variable que le pasemos(en este caso celular2))
#marca es una variable
#marca es otra varible que es a la que vamos a enpaquetar

celular21 = celularr("samsung","S23","48MP")
celular22 = celularr("apple","15 Pro","48MP")

celular21.llamar()