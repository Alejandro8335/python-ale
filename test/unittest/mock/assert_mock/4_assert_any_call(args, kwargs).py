from unittest.mock import Mock
# Verifica que el mock fue llamado en algún momento con esos argumentos 
# (no necesariamente la última).
client = Mock()
client("esp32_ip", port=8080)
client("esp32_ip2", port=9090)

client.assert_any_call("esp32_ip", port=8080)   # ✅ pasa