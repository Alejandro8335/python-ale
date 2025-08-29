
class persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,new_nombre):
        self.__nombre = new_nombre
        
    @nombre.deleter
    def nombre(self):
        del self.__nombre

        
ale = persona("ale",15)     

nombre = ale.nombre
print(nombre)

ale.nombre = "pepe"

nombre = ale.nombre
print(nombre)

del nombre

print(nombre)