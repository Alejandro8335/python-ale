
class auto():
    def __init__(self):
        self._estado = "apagado"
        
    def enceder(self):
        self._estado = "encendido"
        print("el auto esta encendido")
        
    def conducir(self):
        if self._estado == "apagado":
            self.enceder()
        print("conduciendo el auto")
            
mi_auto = auto()
mi_auto.conducir()