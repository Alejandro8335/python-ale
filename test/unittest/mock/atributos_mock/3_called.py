# Qué es: un flag booleano (True o False) que indica si el mock fue llamado al menos una vez.

# Diferencia con call_count:

# call_count → te dice cuántas veces fue llamado.

# called → simplemente te dice si fue llamado alguna vez.

from unittest.mock import Mock

client = Mock()

print(client.called)   # False (todavía no fue llamado)

client("esp32_ip", port=8080)

print(client.called)   # True (ya fue llamado al menos una vez)