# pytest_sessionfinish (qué es)
# pytest_sessionfinish(session, exitstatus) es el hook que Pytest llama al final de 
# toda la sesión de tests, después de que se hayan ejecutado todos los tests y sus
# teardown asociados. Sirve para ejecutar tareas de limpieza global, cerrar 
# recursos compartidos, enviar reportes finales o desregistrar plugins

# conftest.py
class client:
    def __init__(self, api_key):
        self.api_key = api_key
    def close(self):
        print("Cliente cerrado")

def pytest_sessionfinish(session, exitstatus):
    # ejemplo: cerrar cliente compartido si existe
    client_obj = getattr(session.config, "my_client", None)
    if client_obj is not None:
        client_obj.close()
        print("Cliente externo cerrado")

def pytest_sessionfinish(session, exitstatus):
    # ejemplo: desactivar o notificar plugin de logging
    logging_plugin = session.config.pluginmanager.get_plugin("logging-plugin")
    if logging_plugin is not None:
        logging_plugin.disable()
        print("Logging plugin deshabilitado")

def pytest_sessionfinish(session, exitstatus):
    # ejemplo: registrar estado final en el log
    session.config._log.info(f"Fin de sesión de tests. Exit status: {exitstatus}")
    # _log.info = llamar al logger _log para registrar un mensaje de nivel INFO
class MyPlugin:
    def pytest_runtest_setup(self, item):
        pass

def pytest_sessionfinish(session, exitstatus):
    # ejemplo: desregistrar plugin personalizado
    try:
        session.config.pluginmanager.unregister("myplugin")
    except Exception:
        pass