# create_autospec

# Crea un mock basado en un objeto real (función, clase, módulo).

# El mock respeta la firma del objeto original: si llamas con argumentos incorrectos, 
# lanza un error.

# Esto ayuda a que tus tests sean más realistas y evita que pases parámetros que el objeto 
# real nunca aceptaría.

from unittest.mock import create_autospec

def sumar(a, b):
    return a + b

# Creamos un mock que respeta la firma de sumar
mock_sumar = create_autospec(sumar, return_value=10)

print(mock_sumar(2, 3))   # → 10

# Si llamo con argumentos incorrectos:
try:
    mock_sumar(2)   # Falta un argumento
except TypeError as e:
    print(e)        # → TypeError: missing a required argument

############################################################################

class Servicio:
    def obtener(self, clave):
        return f"valor de {clave}"

# Mock que respeta la firma de Servicio
mock_servicio = create_autospec(Servicio)
mock_servicio.obtener.return_value = "mockeado"

print(mock_servicio.obtener("x"))   # → "mockeado"

# Llamada incorrecta
try:
    mock_servicio.obtener()   # Falta argumento
except TypeError as e:
    print(e)                  # → TypeError

############################################################################

# Diferencia clave
# Un Mock normal acepta cualquier llamada, incluso con argumentos inexistentes.

# Un create_autospec valida la firma real y te protege de errores silenciosos en tus tests.