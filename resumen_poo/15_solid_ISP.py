
#isp,Principio de segregación de interfaz
#Interface Segregation Principle

#en este caso con "interfaz" nos referimos a las clases abstractas

from abc import ABC,abstractmethod

#class Trabajador(ABC):
#    @abstractmethod
#    def comer(self):
#       pass
    
#    def Trabajar(self):
#        pass
    
#    def Dormir(self):
#        pass
    
#class Humano(Trabajador):
#    def comer(self):
#        print("el humano esta comiendo")
 
#    def Trabajar(self):
#        print("el humano esta trabajando")
 
#    def Dormir(self):
#        print("el humano esta dormiendo")
    
#class Robot(Trabajador):
#    def comer(self):
#        print("el robot esta comiendo")

#    def Trabajar(self):
#        print("el robot esta trabajando")

#   def Dormir(self):
#        print("el robot esta dormiendo")
        
#esto esta mal 

class Trabajador(ABC):
    @abstractmethod
    def Trabajar(self):
        pass
    
class Comedor(ABC):
    @abstractmethod
    def Comer(self):
        pass
    
class Durmiente(ABC):
    @abstractmethod
    def Dormir(self):
        pass
class Humano(Trabajador,Durmiente,Comedor):
    def Comer(self):
        print("el humano esta comiendo")
 
    def Trabajar(self):
        print("el humano esta trabajando")
 
    def Dormir(self):       
        print("el humano esta dormiendo")
        
class Robot(Trabajador):
    def Trabajar(self):
        print("el robot esta trabajando")

robot = Robot()
robot.Trabajar()

humano = Humano()
humano.Trabajar()

#establece que las clases no deben depender de interfaces que no utilizan.

#En otras palabras, una interfaz grande y 
# generalista puede obligar a las clases que la implementan a depender de métodos que no necesitan,
# lo que genera acoplamiento innecesario y dificulta la mantenibilidad.

#señales:
#Interfaces demasiado grandes: Si tienes una clase con una interfaz que contiene muchos métodos, 
#revisa si todas las clases que la implementan realmente usan todos esos métodos.

#Implementaciones con métodos innecesarios: Si una clase implementa una interfaz 
#y se ve obligada a definir métodos que no necesita, es una señal de que la interfaz está mal diseñada.

#Uso de múltiples interfaces específicas: Si una única interfaz está agrupando demasiadas responsabilidades, 
#considera dividirla en interfaces más pequeñas y 
#especializadas para que cada clase implemente solo las que realmente necesita.