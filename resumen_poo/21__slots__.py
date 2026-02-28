# En Python, __slots__ es una característica especial que se usa dentro de las clases. 
# Su propósito principal es optimizar memoria y restringir qué atributos pueden tener las instancias.

# ¿Qué significa esto?
# Normalmente, cada objeto en Python guarda sus atributos en un diccionario interno (__dict__).

# Eso permite agregar atributos nuevos dinámicamente, pero consume más memoria.

# Si definís __slots__, le decís a Python exactamente qué atributos va a tener la clase.

# Como resultado:

# Se evita crear el diccionario interno.

# Se ahorra memoria (especialmente útil si vas a tener miles o millones de instancias).

# No se pueden agregar atributos que no estén listados en __slots__.

# Ejemplo conceptual
# Imaginá una clase Persona con __slots__ = ("nombre", "edad").

# Cada objeto de esa clase solo puede tener esos dos atributos.

# Si intentás asignar otro atributo, Python lanza un error.

# La ventaja es que cada objeto ocupa menos memoria que una clase normal.

# ¿Cuándo conviene usarlo?
# Cuando vas a crear muchísimas instancias y querés ahorrar memoria.

# Cuando querés controlar estrictamente qué atributos puede tener una clase.

# No es tan útil si solo vas a tener pocas instancias o si necesitás flexibilidad para agregar atributos dinámicamente.

# En resumen: __slots__ es como decirle a Python “mis objetos van a tener solo estos atributos, 
# nada más”. Eso los hace más livianos y rápidos de acceder, pero menos flexibles. 

#########################################################################################################

class Persona:
    __slots__ = ("nombre", "edad")  # solo se permiten estos atributos

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("Alejandro", 25)
print(p.nombre, p.edad)  # OK

# Intentar agregar un atributo que no está en __slots__
try:
    p.ciudad = "Rosario"  # ERROR: AttributeError
except AttributeError as e:
    print(e)    # 'Persona' object has no attribute 'ciudad' and no __dict__ for setting new attributes

# 👉 Aquí, la clase Persona solo puede tener nombre y edad. 
# No se puede agregar nada más. Esto ahorra memoria y restringe los atributos.

#########################################################################################################

class Animal:
    __slots__ = ("especie",)

    def __init__(self, especie):
        self.especie = especie

class Perro(Animal):
    __slots__ = ("raza",)

    def __init__(self, especie, raza):
        super().__init__(especie)
        self.raza = raza

perro = Perro("Canino", "Labrador")
print(perro.especie, perro.raza)  # OK

# Intentar agregar otro atributo
try:
    perro.color = "Marrón"  # ERROR: AttributeError
except AttributeError as e:
    print(e)    # 'Perro' object has no attribute 'color' and no __dict__ for setting new attributes

#########################################################################################################

# La clave está en que __slots__ solo conviene cuando realmente tenés muchas instancias de una clase.

# Si vos definís una clase con __slots__ y después creás una sola instancia, 
# el ahorro de memoria es mínimo, casi imperceptible. La diferencia se nota recién cuando tenés miles o millones de objetos, 
# porque cada uno evita crear su propio diccionario interno (__dict__).

# Entonces:

# Si no necesitás flexibilidad (o sea, no vas a agregar atributos dinámicamente) y vas a tener muchísimos objetos, __slots__ es una gran ventaja.

# Si solo vas a tener uno o unos pocos objetos, no te conviene complicar la clase con __slots__, 
# porque el beneficio es insignificante y perdés la posibilidad de agregar atributos extra si alguna vez lo necesitás.

# En otras palabras:

# Una sola instancia: no vale la pena, el ahorro es mínimo.

# Muchas instancias: sí vale la pena, porque cada objeto ocupa menos memoria y el ahorro se multiplica.

#########################################################################################################

# cada instancia tiene un diccionario interno (__dict__) donde se guardan sus atributos, 
# y desde fuera se puede modificar o incluso inyectar atributos nuevos. Eso da mucha flexibilidad, pero también significa que cualquiera puede alterar el objeto de formas que quizás no quieras.

# __slots__ justamente se inventó para limitar eso. Al definir __slots__, 
# le decís a Python: “mis objetos solo pueden tener estos atributos, nada más”. Entonces:

# Se elimina el __dict__ de cada instancia.

# No se pueden agregar atributos arbitrarios desde afuera.

# El objeto queda más “cerrado” y controlado.

# Por ejemplo, si definís una clase con __slots__ = ("nombre", "edad"), 
# cualquier intento de hacer obj.ciudad = "Rosario" va a dar un AttributeError. 
# Eso evita que alguien desde fuera meta atributos inesperados.

# En resumen:

# Si te molesta que se pueda modificar el __dict__ y no necesitás flexibilidad, 
# sí conviene usar __slots__, incluso aunque tengas pocas instancias.

# El ahorro de memoria es un beneficio extra, 
# pero lo más importante en tu caso sería la restricción de atributos: 
# con __slots__ ya no se puede modificar la clase desde afuera de manera arbitraria.