
class Gato():
    def sonido(self):
        return "miau"
     
class Perro():
    def sonido(self):
        return "guau"
    
def hacer(animal):
        print(animal.sonido())
        
gato = Gato()
perro = Perro()

hacer(perro)
print(gato.sonido())