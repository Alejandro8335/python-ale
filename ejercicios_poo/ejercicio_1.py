
class estudiantes:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print("estudiando...")  
nombre = input("dame tu nombre: ")
edad = input("dame tu edad: ")
grado = input("dame tu grado: ")

estudiante = estudiantes(nombre,edad,grado)

print(f"""
      datos del estudiante:
      nombre: {estudiante.nombre}
      edad: {estudiante.edad}
      nombre: {estudiante.nombre}
      """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()