# Name mangling es el mecanismo de Python que renombra internamente atributos y 
# métodos que comienzan con doble guion bajo __ para evitar colisiones de nombres entre clases y 
# sus subclases. No convierte nada en privado absoluto; 
# lo que hace es dificultar el acceso o la sobrescritura accidental desde fuera de la clase.


# Si definís __atributo o __metodo dentro de una clase Clase, 
# Python lo transforma internamente en _Clase__atributo o _Clase__metodo.


# Esto evita que una subclase que declare __metodo sobrescriba sin querer el método de la clase base, 
# porque sus nombres internos serán distintos.

class Base:
    def __secreto(self):
        print("Base secreto")

    def llamar(self):
        self.__secreto()

class Sub(Base):
    def __secreto(self):
        print("Sub secreto")

b = Base()
b.llamar()          # imprime "Base secreto"

s = Sub()
s.llamar()          # sigue imprimiendo "Base secreto"
# Acceso directo (no recomendado) al método mangled:
b._Base__secreto()  # imprime "Base secreto"
s._Sub__secreto()   # imprime "Sub secreto"
s._Base__secreto()  # imprime "Base secreto"

# El objeto b sigue siendo la instancia de Base.

# Lo que cambia no es el objeto, sino el nombre del atributo dentro de la clase.

# Python no guarda el método como __secreto, sino como _Base__secreto.

# Entonces, cuando hacés b._Base__secreto(), estás accediendo al mismo objeto b, 
# pero usando el nombre interno que Python generó.

# ⚠️ funciona con atributos ⚠️

def secreto():print("secreto desde afuera")

b._Base__secreto = secreto
b._Base__secreto()  # secreto desde afuera