# pytest_sessionstart Qué es?
# pytest_sessionstart(session) es un hook de Pytest que se ejecuta cuando arranca 
# la sesión de tests, justo después de la configuración inicial y antes de la 
# recolección de tests. Sirve para ejecutar código que debe correr una sola vez al 
# inicio de toda la sesión de pruebas.

#######################################################

# Parámetro session Qué contiene
# session es una instancia que representa la sesión de Pytest.

# Contiene información sobre la ejecución actual, acceso a config vía 
# session.config, y métodos/atributos relacionados con la colección y ejecución de 
# tests.

# No es una fixture: es el objeto que Pytest pasa al hook.

#######################################################

# Momento exacto de ejecución
# Se llama una vez al inicio de la sesión, después de que Pytest haya procesado 
# opciones y registrado plugins, y antes de la recolección de tests.

# Orden típico relativo a otros hooks: pytest_configure(config)
# → pytest_sessionstart(session) → recolección → ejecución de tests.

#######################################################
# conftest.
class client:
    def __init__(self,api_key):
        pass
def pytest_sessionstart(session):
    # ejemplo: inicializar cliente compartido
    session.config.my_client = client(api_key=session.config.getoption("--api-key"))
    print("Cliente externo inicializado")
    
def pytest_sessionstart(session):
    # ejemplo: activar modo especial o registrar métricas
    session.config.pluginmanager.get_plugin("logging-plugin").enable()

def pytest_sessionstart(session):
    session.config._log.info("Inicio de sesión de tests")

class MyPlugin:
    def pytest_runtest_setup(self, item):
        # comportamiento por test
        pass

def pytest_sessionstart(session):
    session.config.pluginmanager.register(MyPlugin(), name="myplugin")