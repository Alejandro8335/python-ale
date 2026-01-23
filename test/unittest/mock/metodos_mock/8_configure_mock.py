# En Python, dentro de unittest.mock, el método configure_mock sirve para configurar atributos o 
# valores de retorno de un mock después de haberlo creado. 
# Es básicamente una forma más ordenada de asignar propiedades sin tener que hacerlo 
# manualmente una por una.

# 🔧 ¿Cómo funciona?
# Se llama sobre un objeto Mock o MagicMock.

# Recibe argumentos con nombre (kwargs) que se aplican como configuración del mock.

# Es equivalente a hacer asignaciones directas, pero más compacto y expresivo.

from unittest.mock import Mock

# Creamos un mock vacío
m = Mock()

# Configuramos atributos y valores de retorno
m.configure_mock(return_value=42, nombre="Alejandro")

# Ahora el mock se comporta así:
print(m())          # 42
print(m.nombre)     # "Alejandro"

################################################################

from unittest.mock import Mock

# Mock de una función
api_call = Mock()

# Configuramos varios aspectos
api_call.configure_mock(
    return_value={"status": "ok"},
    called=True,
    call_count=3
)

print(api_call())          # {'status': 'ok'}
print(api_call.called)     # True
print(api_call.call_count) # 3