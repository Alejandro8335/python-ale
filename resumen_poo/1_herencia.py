
class persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.naciomalidad = nacionalidad
    def hablar(self):
        print("hola,estoy trabajando")

class empleados(persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
    #reescribir una funcion
    def hablar(self):
        print(f"hola,soy un {self.trabajo}")
roberto = empleados("roberto",43,"argentino","programador",100000)

print(roberto.trabajo)
roberto.hablar()