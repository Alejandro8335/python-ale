# getoption(name)
# Qué hace: Devuelve el valor de una opción pasada por CLI
# (pytest --verbose, pytest --maxfail=2, etc.).

# Para qué sirve: Permite que fixtures, hooks o plugins adapten su comportamiento
# según los flags usados al ejecutar Pytest.

def pytest_configure(config):
    if config.getoption("verbose"): # devuelve el numero de veces que aparece
        print("Modo verboso activado")