# Atributos personalizados
# Qué hace: Puedes adjuntar atributos arbitrarios al objeto config.

# Para qué sirve: Compartir objetos globales (clientes HTTP, conexiones DB, configuraciones externas) entre fixtures y tests.

import pytest

class MyApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

def pytest_configure(config):
    config.my_client = MyApiClient(base_url="http://localhost")

@pytest.fixture
def client(request):
    return request.config.my_client
#######################################################
# request es un fixture incorporado de pytest que proporciona información y 
# utilidades sobre el contexto de ejecución del test (por ejemplo, el objeto config,
# el nombre del test, el scope, y opciones de línea de comandos)