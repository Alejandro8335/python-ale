# test_usefixtures.py
import pytest

@pytest.fixture
def setup_db():
    print("\n[SETUP] Conectando a la base de datos")
    yield "hola"
    print("\n[TEARDOWN] Cerrando conexión")
    # Antes del yield → se ejecuta el setup.
    # El valor del yield → es lo que recibe el test si lo usa como argumento.
    # Después del yield → se ejecuta el teardown cuando termina el test.
@pytest.mark.usefixtures("setup_db")
def test_query():
    # No recibe setup_db como argumento, pero igual se ejecuta
    assert 1 + 1 == 2
    
def test_args(setup_db):
    # El test recibe el valor retornado por el fixture
    print(f"Valor recibido dentro del test: {setup_db}")
    assert setup_db == "hola"
# Con argumento: recibís el valor del fixture y lo podés usar en el test.

# Con usefixtures: el fixture se ejecuta igual (setup/teardown), pero no recibís el valor. Solo sirve para efectos secundarios.