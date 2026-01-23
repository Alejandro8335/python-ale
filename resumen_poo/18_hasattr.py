# ¿Qué es hasattr?
# hasattr(objeto, "atributo")


# Devuelve:

# True → si el objeto tiene ese atributo

# False → si no existe

class A:
    pass

a = A()
# Evitar errores cuando un atributo puede no existir todavía.
hasattr(a, "x")   # False

a.x = 10

hasattr(a, "x")   # True