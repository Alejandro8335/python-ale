# addinivalue_line(key, line)
# Qué hace: Añade dinámicamente una línea a la configuración ini.

# Para qué sirve: Registrar marcadores personalizados y evitar warnings de 
# Pytest cuando se usan sin estar declarados.

def pytest_configure(config):
    config.addinivalue_line("markers", "slow: marca tests que tardan mucho")