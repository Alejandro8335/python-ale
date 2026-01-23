# Qué es: es una lista que registra todas las llamadas realizadas al mock y a sus atributos/métodos.

# Incluye:

# Llamadas directas al mock (client(...)).

# Llamadas a métodos o atributos del mock (client.connect(), client.disconnect()).

# Cada entrada es un objeto call que describe la invocación.

from unittest.mock import Mock

client = Mock()

# Llamadas directas
client("esp32_ip", port=8080)

# Llamadas a métodos simulados
client.connect("wifi")
client.disconnect()

print(client.mock_calls)
# [
#   call('esp32_ip', port=8080),
#   call.connect('wifi'),
#   call.disconnect()
# ]