# Qué es: guarda los argumentos de la última llamada que recibió el mock.

# Formato: es una tupla (args, kwargs) donde:

# args → lista de argumentos posicionales.

# kwargs → diccionario de argumentos con nombre

from unittest.mock import Mock

client = Mock()

# Llamamos al mock con argumentos
client("esp32_ip", port=8080)

print(client.call_args)
# Resultado: call('esp32_ip', port=8080)

# Podemos acceder a los detalles
args, kwargs = client.call_args
print(args)    # ('esp32_ip',)
print(kwargs)  # {'port': 8080}
