from unittest.mock import Mock
#  Verifica que el mock nunca fue llamado.
client = Mock()
client.assert_not_called()   # ✅ pasa