import pytest
# Cuando definís un fixture, podés indicar con el parámetro scope cuánto tiempo 
# dura y cuántas veces se ejecuta durante la corrida de tests. Las opciones son:

# Sin scope: equivale a scope="function".

# Regla práctica
# scope="module" + @pytest.mark.parametrize → fixture creado 1 vez por módulo, reutilizado en todas las ejecuciones parametrizadas.

# scope="module" + fixture(params=...) → fixture creado 1 vez por cada parámetro (por módulo), y cada instancia se comparte entre tests.

# scope="function" → fixture creado en cada ejecución del test, incluyendo cada caso parametrizado.
#######################################################

# Duración: se crea y destruye para cada test individual.
# Uso típico: datos frescos y aislados en cada prueba.
@pytest.fixture(scope="function")
def usuario():
    print("Creo usuario nuevo")
    return {"nombre": "Alejandro"}

#######################################################

# Duración: se crea una vez por clase de test y se comparte entre todos los métodos 
# de esa clase.
# Uso típico: cuando los tests dentro de una clase pueden compartir un mismo recurso.

@pytest.fixture(scope="class")
def conexion_api():
    print("Conecto API")
    return "conexion"

#######################################################

# Duración: se crea una vez por archivo de test (módulo).
# Uso típico: recursos pesados que pueden ser compartidos por todos los tests del 
# archivo.

@pytest.fixture(scope="module")
def recurso():
    print("SETUP recurso")
    return {"status": "ok"}

@pytest.mark.parametrize("x", [1, 2, 3])
def test_ejemplo(recurso, x):
    print("TEST con x =", x, "y recurso id:", id(recurso))# es el mismo objeto
    assert recurso["status"] == "ok"


#######################################################

# Duración: se crea una sola vez en toda la ejecución de pytest.
# Uso típico: inicializaciones globales, como levantar un servidor o cargar un 
# dataset grande.

@pytest.fixture(scope="session")
def servidor():
    print("Levanto servidor")
    yield
    print("Apago servidor")

#######################################################

# Duración: se crea una vez por paquete de tests
# Uso típico: datos compartidos entre todos los tests del mismo paquete
@pytest.fixture(scope="package")
def usuario():
    print("Creo usuario del paquete")
    return {"nombre": "Alejandro"}