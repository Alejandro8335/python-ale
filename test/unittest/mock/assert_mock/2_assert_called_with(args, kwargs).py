from unittest.mock import Mock
# Verifica que la última llamada al mock fue con esos argumentos.
client = Mock()
client("esp32_ip", port=8080)
client.assert_called_with("esp32_ip", port=8080)   # ✅ pasa