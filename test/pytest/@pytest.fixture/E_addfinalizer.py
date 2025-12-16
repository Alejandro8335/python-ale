# ¿Qué son los finalizers?
# Son una forma de definir código de limpieza (teardown) en un fixture.

# Se ejecutan después del test que usó el fixture.

# Son una alternativa al uso de yield.
import pytest

@pytest.fixture
def recurso(request):
    print("Creo recurso")

    def cleanup():
        print("Libero recurso")

    request.addfinalizer(cleanup)
    return "recurso"

def test_uso_recurso(recurso):
    print("Test usando", recurso)

# Flujo:
# Se crea el recurso.

# Se corre el test.

# Al terminar, pytest ejecuta la función cleanup.
# Salida:
# Creo recurso
# Test usando recurso
# Libero recurso

#######################################################

# En resumen:
# yield → más simple y directo.
# addfinalizer → más flexible, permite múltiples finalizers o lógica más compleja.

#######################################################

# Atributo / Método -> Para qué sirve
# request.config -> Acceder a la configuración global (pytest.Config)
# request.node -> Información del test actual (nombre, markers, path)
# request.fixturenames -> Lista de fixtures disponibles
# request.getfixturevalue(name) -> Obtener otra fixture manualmente
# request.param -> Valor del parámetro si la fixture es parametrizada
# request.addfinalizer(func) -> Registrar teardown para la fixture