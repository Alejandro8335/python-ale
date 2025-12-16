# rootpath / rootdir
# Qué hace: Directorio raíz detectado por Pytest (donde está pytest.ini o el proyecto).

# Para qué sirve: Construir rutas relativas de forma consistente, sin depender de dónde se ejecute el comando.

def pytest_configure(config):
    print("Directorio raíz:", config.rootpath)