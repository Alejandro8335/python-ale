
class personas:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")

class estudiante(personas):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado
        
    def mostrar_grado(self):
        print(f"grado: {self.grado}")

estudiant = estudiante("ale",15,2)
estudiant.mostrar()
estudiant.mostrar_grado()