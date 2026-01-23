from unittest.mock import Mock
# Verifica que el mock fue llamado al menos una vez.
client = Mock()
client("esp32_ip")
client.assert_called()   # ✅ pasa