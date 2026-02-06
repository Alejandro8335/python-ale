# Qué hace super()
# Devuelve un proxy que representa la siguiente clase en el MRO para la combinación de la clase y la instancia desde donde se llama.

# Cuando llamás super().metodo(...), Python busca metodo a partir de esa siguiente clase en el MRO, y lo ejecuta si existe.

# No significa “llamar al padre directo”; significa “llamar al siguiente en el orden de resolución de métodos”.

# Formas comunes: super().metodo(...) (Python 3) o super(Clase, self).metodo(...) (forma explícita).

# Uso práctico: encadenar __init__ y otros métodos en jerarquías (incluida la herencia múltiple) sin nombrar clases concretas, evitando duplicar llamadas.

#####################################################################################################################
class A:
    def fun(self): print("A")

class B(A):
    def fun(self):
        print("B")
        super().fun()

class C(A):
    def fun(self):
        print("C")
        super().fun()

class D(B, C):
    def fun(self):
        print("D")
        super().fun()

D().fun()
print(D.mro())

#####################################################################################################################
# super() = “delegar la llamada al siguiente método en la cadena de resolución (MRO)”.

#####################################################################################################################
# Cuando invocás super().función(), Python no salta directamente a la clase padre inmediata, 
# sino que arranca la búsqueda en la siguiente clase del MRO respecto de la clase actual.

# Si esa siguiente clase no tiene el método que estás pidiendo, Python sigue recorriendo el MRO hasta encontrarlo.

# En otras palabras: super() no se queda trabado, 
# sino que avanza por la cadena de resolución hasta dar con la primera definición del método que coincida.

# Si ninguna clase en el MRO lo define, lanza un AttributeError