# ¿Qué es?
# raise se usa para lanzar una excepción (error) de forma explícita.

# Sirve para detener el flujo normal del programa cuando ocurre una condición inválida.

# Sintaxis
# raise NombreDelError("mensaje descriptivo")

def set_edad(edad):
    if edad < 0:
        raise ValueError("Edad inválida: no puede ser negativa")
    return edad

# print(set_edad(-1))

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b

print(dividir(100,0))