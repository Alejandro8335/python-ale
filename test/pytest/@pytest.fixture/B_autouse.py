# El fixture se ejecuta automáticamente en todos los tests dentro de su alcance, 
# aunque no lo nombres.
import pytest

@pytest.fixture(autouse=True)
def limpiar_cache():
    print("Cache limpiada")

def test_a():
    print("Ejecutando test A")

def test_b():
    print("Ejecutando test B")

# Cache limpiada
# Ejecutando test A
# Cache limpiada
# Ejecutando test B

#######################################################

# Sin autouse: el fixture se usa solo si lo pedís explícitamente en el test.

# Con autouse: el fixture se aplica siempre y automáticamente a todos los tests del 
# alcance definido.