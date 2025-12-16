# Respuesta breve: Usa fixtures para preparar y limpiar recursos por test o por 
# scope (function/module/session); usa pytest_configure para inicializar o registrar 
# cosas globales del runner antes de la recolección. pytest_configure no reemplaza a 
# las fixtures, complementa su ámbito y propósito

#######################################################

# getoption(name) -> Leer flags de CLI para condicionar comportamiento
# getini(name) -> Acceder a configuraciones persistentes en pytest.ini
# addinivalue_line() -> Registrar marcadores y evitar warnings
# pluginmanager -> Gestionar plugins y hooks dinámicamente
# rootpath/rootdir -> Obtener el directorio raíz del proyecto
# Atributos personalizados -> Compartir objetos globales entre tests y fixtures