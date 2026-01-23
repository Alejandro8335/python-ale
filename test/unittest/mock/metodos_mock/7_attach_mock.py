# Tienes un mock principal.

# Creas otros mocks secundarios.

# Con attach_mock(submock, nombre) le dices al mock principal:
# “Este mock secundario ahora es tu atributo llamado nombre”.

# De esa forma puedes acceder a él como principal.nombre.

from unittest.mock import Mock

# Mock principal
api = Mock()

# Mock secundario
get_data = Mock()

# Lo adjuntamos como atributo
api.attach_mock(get_data, 'get_data')

# Ahora podemos usarlo como si fuera parte de api
api.get_data("param1")

# Verificamos
print(api.get_data.called)       # True
print(api.get_data.call_args)    # call('param1')

# También queda registrado en el historial del mock principal
print(api.mock_calls)
# [call.get_data('param1')]
