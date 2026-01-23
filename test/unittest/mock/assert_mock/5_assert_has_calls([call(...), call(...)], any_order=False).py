from unittest.mock import Mock
# Verifica que el mock recibió una secuencia de llamadas específicas.

# any_order=True permite que estén en cualquier orden.
from unittest.mock import call

client = Mock()
client("esp32_ip", port=8080)
client("esp32_ip2", port=9090)

client.assert_has_calls([
    call("esp32_ip", port=8080),
    call("esp32_ip2", port=9090)
])   # ✅ pasa