
class personaje:
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self):
        return f"{self.nombre}(fuerza: {self.fuerza},velocidad: {self.velocidad})"
    
    def __add__(self,otro):
        nombre2 = self.nombre + "-" + otro.nombre
        fuerza2 = round(((self.fuerza + otro.fuerza)/2)**1.5)
        velocidad2 = round(((self.velocidad + otro.velocidad)/2)**1.5)
        return personaje(nombre2,fuerza2,velocidad2)

goku = personaje("goku",100,100)
vegeta = personaje("vegeta",99,99)
jiren = personaje("jiren",130,140)
suma = goku + vegeta
suma2 = suma + jiren
print(suma2)