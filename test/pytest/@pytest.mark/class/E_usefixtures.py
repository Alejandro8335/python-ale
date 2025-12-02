import pytest

@pytest.fixture
def db():
    print("\n[setup] creando conexión")
    yield
    print("\n[teardown] cerrando conexión")

@pytest.mark.usefixtures("db")
class TestDatabase:
    def test_insert(self):
        print("probando insert...")

    def test_delete(self):
        print("probando delete...")
        
# Cuando lo aplicás a una clase, el fixture se inyecta automáticamente en todos 
# los métodos de test de esa clase, aunque no lo declares como argumento 
# en cada uno.