
class persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self._edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,new_nombre):
         self.__nombre = new_nombre
        
ale = persona("lucas",15)     
nombre = ale.get_nombre()
print(nombre)

ale.set_nombre("ale")
nombre = ale.get_nombre()
print(nombre)