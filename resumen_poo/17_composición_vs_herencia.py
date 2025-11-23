# Herencia
# Usás herencia cuando:

# Tu clase es un tipo especial de otra clase.

# Existe una relación “es un” (is-a).

# Querés reutilizar comportamiento y extenderlo.

class Personaje:
    def mover(self):
        print("Se mueve")

class Enemigo(Personaje):  # Un enemigo ES un personaje
    def atacar(self):
        print("Ataca")
        
# Enemigo hereda de Personaje.
# Tiene todo lo que tiene Personaje + su propio método atacar.

# Composición (crear objetos dentro del __init__)
# Usás composición cuando:

# Tu clase tiene otra clase como parte de ella.

# Existe una relación “tiene un” (has-a).

# Querés combinar funcionalidades sin necesidad de heredar.

class Arma:
    def disparar(self):
        print("Bang!")

class Enemigo:
    def __init__(self):
        self.arma = Arma()  # Un enemigo TIENE un arma

    def atacar(self):
        self.arma.disparar()
        
# Enemigo no es un Arma, pero tiene un arma.
# Usás composición para que el enemigo pueda disparar.


# Regla práctica
# Herencia → cuando la relación es “es un” y querés extender comportamiento.

# Composición → cuando la relación es “tiene un” y 
# querés usar funcionalidades de otra clase como parte interna.