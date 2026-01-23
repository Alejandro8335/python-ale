from unittest.mock import Mock
# Verifica que el mock fue llamado exactamente una vez.
client = Mock()
client("esp32_ip")
client.assert_called_once()   # ✅ pasa
