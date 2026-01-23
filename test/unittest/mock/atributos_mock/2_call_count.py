# Qué es: indica el número total de veces que el mock fue llamado.

# Tipo de dato: un entero (int).

# Diferencia con call_args_list:

# call_args_list → te muestra el detalle de cada llamada.

# call_count → solo te da el número total.

from unittest.mock import Mock

client = Mock()

# Llamamos varias veces
client("esp32_ip", port=8080)
client("esp32_ip2", port=9090)
client("esp32_ip3", port=10000)

print(client.call_count)  # 3
