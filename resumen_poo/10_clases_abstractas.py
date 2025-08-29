
from abc import ABC,abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractclassmethod
    def Actividad(self):
        pass
    
    def Presentarse(self):
        print(f"hola me llamo: {self.nombre} y tengo {self.edad} años")
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    def Actividad(self):
        print(f"estoy estudiando: {self.actividad}")
        
class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    def Actividad(self):
        print(f"mi trabajo se trata de la {self.actividad}")
        
        
ale = Estudiante("ale",15,"hombre","programacion")
dalto = Trabajador("lucas",21,"hombre","programacion") 
ale.Presentarse()
ale.Actividad()
dalto.Presentarse()
dalto.Actividad()

#ABC es la clase base para definir una clase abstracta.
#Una clase abstracta no puede ser instanciada directamente y 
#generalmente sirve como plantilla para otras clases.

#abstractmethod es un decorador que marca un método como abstracto. 
#Un método abstracto no tiene implementación en la clase base y 
#debe ser implementado por cualquier subclase que herede de esta clase.