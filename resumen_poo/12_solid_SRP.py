
#srp,principio de reponsabilidad unico
#single responsibility principle

class Tanque:
    def __init__(self):
        self.combustible = 100
        
    def Agregar(self, cantidad):
        self.combustible += cantidad    
        
    def Obtener(self):
        return self.combustible
    
    def Usar(self, cantidad):
        if cantidad > self.combustible:
            print("No puedes usar más combustible del disponible")
        else:
            self.combustible -= cantidad

class Auto:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
        
    def Mover(self, distancia):
        if self.tanque.Obtener() >= distancia / 2:
            self.posicion += distancia
            self.tanque.Usar(distancia / 2)
            return "Has movido el auto exitosamente"
        else:
            return "No hay suficiente combustible"
            
    def Posicion(self):
        return self.posicion


tanque = Tanque()
auto = Auto(tanque)

print(auto.Posicion())
print(auto.Mover(10))
print(auto.Posicion())
print(auto.Mover(20))
print(auto.Posicion())
print(auto.Mover(60))
print(auto.Posicion())
print(auto.Mover(100))
print(auto.Posicion())
print(auto.Mover(100))
print(auto.Posicion())
 
#senales:
#Tiene demasiados métodos que hacen cosas no relacionadas.

#Maneja múltiples aspectos en lugar de enfocarse en una sola responsabilidad.

#Está difícil de extender o modificar sin afectar otras partes del código.