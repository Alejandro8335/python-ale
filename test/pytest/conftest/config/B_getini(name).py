# getini(name)
# Qué hace: Devuelve valores definidos en archivos de configuración
# (pytest.ini, tox.ini, pyproject.toml).

# Para qué sirve: Centraliza configuraciones persistentes, como testpaths, addopts,
# markers.

def pytest_configure(config):
    paths = config.getini("testpaths")
    print("Pytest buscará tests en:", paths)