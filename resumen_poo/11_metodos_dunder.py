
#empienzan y terminan con los __

class persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
     
    #le explico la forma en que me lo tiene que devolver   
    def __str__(self):
        return f"persona(nombre={self.nombre},edad={self.edad})"
    
    def __repr__(self):
         return f'Persona("{self.nombre}", {self.edad})'
    
    def __add__(self,otro):
        nuevo_valor =self.edad + otro.edad
        return persona(self.nombre+otro.nombre,nuevo_valor)
        
        
ale = persona("ale",15)
dalto = persona("dalto",30)
pedro = persona("pedro",20)

resultado = ale + dalto + pedro
print(resultado.edad)