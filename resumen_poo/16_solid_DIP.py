
#dip,principio de inversión de dependencia
#dependency invension principle

# class Dicionario:
#     def Verificar(self,palabra):
#         #logica para verificar palabras
#         pass
    
# class Corrector:
#     def __init__(self):
#         self.diccionario = Dicionario()
        
#     def Corregir(self,texto):
#         #usamos el diccionario para corregir el texto
#         pass

from abc import ABC,abstractmethod

class Verificador(ABC):
    @abstractmethod
    def Verificar(self,palabra):
        #logica para verificar palabras
        pass
    
class Diccionario(Verificador):
    def Verificar(self, palabra):
        #logica para verificar palabras si estan en el diccionario
        pass
    
class Corrector:
    def __init__(self,verificador):
        self.verificador = verificador
        
    def corregir(self,texto):
        #usamos el verificadorpara corregir texto
        pass
    
corrector = Corrector(Diccionario())

#modulos alto/bajo nivel:

#Módulo de alto nivel: Es aquel que maneja la lógica más general o estratégica del sistema. 
#Suele contener reglas de negocio y coordinar la interacción entre distintos módulos. 
#Ejemplo: una clase que gestiona pedidos en un sistema de compras.

#Módulo de bajo nivel: Se encarga de tareas más específicas y detalladas dentro del sistema. 
#Suele estar más cerca de la implementación concreta, como el acceso a bases de datos o la manipulación de archivos. 
#Ejemplo: una clase que interactúa con la base de datos para guardar información de los pedidos.

#DIP:

#Los módulos de alto nivel no deben depender de los de bajo nivel. Ambos deben depender de abstracciones.

#Las abstracciones no deben depender de los detalles. Los detalles deben depender de las abstracciones.

#si respondes "sí" a alguna de estas preguntas, es probable que estés violando el DIP:

#¿Tu clase de alto nivel depende directamente de una implementación concreta en lugar de una abstracción 
#(como una interfaz o clase abstracta)?

#¿Estás instanciando objetos de bajo nivel dentro de una clase de alto nivel en lugar de inyectarlos desde afuera?

#¿Un cambio en una clase de bajo nivel obliga a modificar la clase de alto nivel?