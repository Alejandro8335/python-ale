# pluginmanager

# Plugins = extensiones que agregan capacidades.

# Hooks = puntos de conexión donde esas extensiones se enganchan para modificar el 
# comportamiento de pytest.

# Qué hace: Es la instancia de PluginManager que gestiona todos los plugins y 
# hooks de Pytest.

# Para qué sirve: Registrar, desregistrar o inspeccionar plugins en tiempo de 
# ejecución.

class MyPlugin:
    pass
def pytest_configure(config):
    # Registrar un plugin custom
    config.pluginmanager.register(MyPlugin(), "myplugin")