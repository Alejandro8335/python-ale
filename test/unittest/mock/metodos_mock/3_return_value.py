# return_value
# Define el valor fijo que devolverá el mock cada vez que se invoque.

# Es la forma más sencilla de controlar el resultado de una llamada simulada.

# A diferencia de side_effect, no cambia entre llamadas ni lanza excepciones: siempre devuelve lo mismo.

from unittest.mock import Mock

m = Mock()
m.obtener.return_value = {"ok": True}

print(m.obtener())   # → {"ok": True}
print(m.obtener())   # → {"ok": True}  # siempre lo mismo
print(m.obtener)     # → <Mock name='mock.obtener' id='1839095725568'>

# Clase → mock_Clase
# Instancia → mock_Clase.return_value