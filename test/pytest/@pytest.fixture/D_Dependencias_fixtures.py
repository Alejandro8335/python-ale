# Un fixture puede recibir como argumento otro fixture.

# Pytest se encarga de resolver la cadena de dependencias automáticamente.

# Esto permite construir setups más complejos y reutilizables.
import pytest

@pytest.fixture
def usuario():
    return {"nombre": "Alejandro"}

@pytest.fixture
def sesion(usuario):
    return f"Sesión iniciada para {usuario['nombre']}"

def test_sesion(sesion):
    assert "Alejandro" in sesion

#######################################################

@pytest.fixture
def db():
    print("Conecto a la base de datos")
    return "DB"

@pytest.fixture
def usuario(db):
    print("Creo usuario en", db)
    return {"id": 1, "nombre": "Alejandro"}

@pytest.fixture
def sesion(usuario, db):
    print("Inicio sesión en", db)
    return f"Sesión para {usuario['nombre']}"

# Piensa así:

# “Este test necesita un fixture llamado sesion.”

# “¿Ese fixture necesita algo más?”

# “Ah, sesion depende de usuario y de db.”

# “¿Y usuario depende de algo?”

# “Sí, depende de db.”

# “Entonces primero creo db, después usuario, después sesion.”

# Pytest construye una especie de árbol de dependencias y lo resuelve 
# automáticamente.
#######################################################

# Ventaja
# Modularidad: cada fixture hace una sola cosa.

# Reutilización: podés usar usuario en otros tests sin necesidad de sesion.

# Pytest se encarga de la resolución de dependencias.