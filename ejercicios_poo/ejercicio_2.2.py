
class animal:
    def comer(self):
        print("el animal esta comiendo")
        
class ave(animal):
    def volar(self):
        print("el ave esta volando")
    
class mamifero(animal):
    def amamatar(self):
        print("el mamifero esta amamantando")
        
class murcielado(mamifero,ave):
    pass
    
murcielago = murcielado()
murcielago.comer()
murcielago.volar()
murcielago.amamatar()