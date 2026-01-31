# Idea clave
# Namespace = diccionario nombre → referencia a objeto en memoria.  
# La resolución de nombres sigue LEGB: Local → Enclosing → Global → Built‑in.

################################################################################
# mostrando Local, Global y Built‑in
x = "global_x"          # global namespace

def f():
    y = "local_y"       # local namespace de f
    print(y)            # busca en Local -> imprime "local_y"
    print(x)            # no está en local, busca en Global -> imprime "global_x"
    print(len([1,2]))   # no está en L/E/G, busca en Built-in -> usa builtins.len

f()

################################################################################
# Enclosing namespace con función anidada y nonlocal
def outer():
    a = "enclosing_a"   # enclosing namespace para inner
    def inner():
        nonlocal a  # encuentra 'a' en Enclosing
        a = "modificado"
        print(a)        # "modificado"
    inner()
    print(a)            # "modificado"

outer()

################################################################################
# def vs lambda y su relación con el namespace

# def crea un nombre en el namespace al definirla
def doble(x):
    return x * 2

# lambda crea un objeto función; si lo asignas, aparece en el namespace
triple = lambda x: x * 3

print("doble" in globals())   # True
print("triple" in globals())  # True

# lambda anónima sin asignar: no queda en globals
print((lambda x: x+1)(5))     # 6
# no hay nombre en globals para esa función anónima

################################################################################
# del quita la referencia del namespace; liberación depende de referencias restantes
def f(): pass

g = f           # otra referencia al mismo objeto función
del f           # quita 'f' del namespace global
print('f' in globals())  # False
print(g())      # sigue funcionando porque 'g' mantiene la referencia
print('g' in globals())  # True

################################################################################
# Namespace de clase y atributos

class C:
    x = 10      # atributo en el namespace de la clase

    def m(self):
        y = 5   # variable local del método (namespace local al ejecutar m)
        return self.x + y

print(C.__dict__['x'])  # 10  -> namespace de la clase es un dict

################################################################################
# Inspeccionar namespaces en tiempo de ejecución
a = 1
def ejemplo(b):
    c = 3
    print("locals:", locals())   # muestra {'b': 2, 'c': 3}
    print("globals has 'a':", 'a' in globals())

ejemplo(2)
################################################################################

# Nombres son referencias; objetos viven en memoria.

# Un objeto se libera cuando no quedan referencias a él (conteo de referencias + GC para ciclos).

# def crea el objeto función y asigna un nombre en el namespace; lambda crea el objeto función y 
# solo queda en el namespace si lo asignas.

# Búsqueda de nombres: Local → Enclosing → Global → Built‑in.

# Usá globals(), locals() y obj.__dict__ para inspeccionar namespaces.