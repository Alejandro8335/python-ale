
class persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.naciomalidad = nacionalidad
        
    def hablar(self):
        print("hola,estoy trabajando")

class artita:
    def __init__(self,habilidad):
        self.habilidad = habilidad
        
    def mostrar(self):
        print(f"mi habilidad es: {self.habilidad}")

class empleados(persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
    #reescribir una funcion
    def hablar(self):
        print(f"hola,soy un {self.trabajo}")
  
#herencia multiple                  
class empleados_artista(persona,artita):
    def __init__(self, nombre, edad, nacionalidad,habilidad,trabajo,salario):
        super().__init__(nombre, edad, nacionalidad)
        artita.__init__(self,habilidad)
        self.trabajo = trabajo
        self.salario = salario
              
    def presentarse(self):
        return f"{super().mostrar()}"
        #super hace que se acceda a la clase padre osea que no importa si lo redefino abajo
roberto = empleados_artista("roberto",43,"argentino","cantar","programador",100000)


herencia = issubclass(empleados_artista,artita)#true
instancia = isinstance(roberto,persona)#true
print(instancia)

 
