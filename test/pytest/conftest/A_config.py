# Resumen breve: config es el objeto central de configuración de Pytest
# (instancia de pytest.Config) que contiene opciones CLI, valores de ini, y el
# pluginmanager; se usa para leer opciones, registrar marcadores/plugins y exponer
# datos globales antes de la recolección

#######################################################
#######################################################

# Resumen: pytest.Config
# pytest.Config es el objeto central de configuración en Pytest (una instancia de
# pytest.Config) que centraliza las opciones de línea de comandos, los valores de
# ini, y el pluginmanager; se utiliza para leer opciones, registrar marcadores y
# plugins, y exponer datos globales antes y durante la recolección de tests.

# Qué contiene
# Opciones CLI: valores pasados al ejecutar pytest (por ejemplo -k, -q, --maxfail)
# accesibles desde config.getoption(...).

# Valores de ini: configuraciones definidas en pytest.ini, tox.ini o pyproject.toml
# accesibles vía config.getini(...).

# PluginManager: instancia que gestiona plugins, hooks y su registro
# (config.pluginmanager).

# Marcadores registrados: lista de markers y su metadata para validación y
# documentación.

# Rutas y estado global: información sobre el entorno de ejecución, directorios raíz, y opciones globales usadas durante la recolección.

#######################################################
#######################################################

# En este contexto, CLI significa Command-Line Interface
# (Interfaz de Línea de Comandos).

# Cuando ejecutas pytest (u otra herramienta) desde la terminal, puedes pasarle
# opciones o parámetros escritos después del comando. Por ejemplo:

# pytest --verbose --maxfail=2

# pytest → es el programa que se ejecuta.

# --verbose → es una opción de CLI que le dice a pytest que muestre más detalles
# en la salida.

# --maxfail=2 → es otra opción que indica que se detenga después de 2 fallos.