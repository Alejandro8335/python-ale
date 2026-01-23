# Qué es: guarda todas las llamadas que recibió el mock, en orden cronológico.

# Formato: es una lista de objetos call, cada uno con (args, kwargs) de cada invocación.

# Diferencia con call_args:

# call_args → solo la última llamada.

# call_args_list → historial completo de llamadas.

from unittest.mock import Mock

client = Mock()

# Llamamos varias veces al mock
client("esp32_ip", port=8080)
client("esp32_ip2", port=9090)

# Última llamada
print(client.call_args)
# call('esp32_ip2', port=9090)

# Todas las llamadas
print(client.call_args_list)
# [call('esp32_ip', port=8080), call('esp32_ip2', port=9090)]

# Podemos recorrerlas
for call in client.call_args_list:
    args, kwargs = call
    print("args:", args, "kwargs:", kwargs)