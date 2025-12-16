import pytest
# Cuando definís un fixture, podés indicar con el parámetro scope cuánto tiempo 
# dura y cuántas veces se ejecuta durante la corrida de tests. Las opciones son:

# Sin scope: equivale a scope="function".
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
def conexion_db():
    print("Conecto a la base de datos")
    yield
    print("Cierro conexión")

#######################################################

# Duración: se crea una sola vez en toda la ejecución de pytest.
# Uso típico: inicializaciones globales, como levantar un servidor o cargar un 
# dataset grande.

@pytest.fixture(scope="session")
def servidor():
    print("Levanto servidor")
    yield
    print("Apago servidor")