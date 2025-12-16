# ¿Qué es conftest.py?
# Es un archivo especial que pytest reconoce automáticamente.

# Se usa para definir fixtures y hooks comunes que estarán disponibles en todos los 
# tests del directorio y sus subdirectorios.

# No hace falta importar nada: pytest lo detecta por convención.
import pytest

@pytest.fixture(scope="module")
def conexion_db():
    print("Conecto a la base de datos")
    yield 
    print("Cierro conexión")

# Ventajas
# Centralización: no repetís fixtures en cada archivo.

# Reutilización: todos los tests pueden acceder a los mismos recursos.

# Organización: podés tener conftest.py global y otros más específicos por módulo.

#######################################################

# pueden usar tanto los fixtures del conftest.py global como los del conftest.py 
# local.