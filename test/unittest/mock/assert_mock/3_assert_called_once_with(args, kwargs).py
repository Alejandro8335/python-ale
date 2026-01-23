from unittest.mock import Mock
# Verifica que el mock fue llamado una sola vez y con esos argumentos.
client = Mock()
client("esp32_ip", port=8080)
client.assert_called_once_with("esp32_ip", port=8080)   # ✅ pasa