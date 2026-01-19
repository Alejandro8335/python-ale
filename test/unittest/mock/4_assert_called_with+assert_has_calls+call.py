# assert_called_with
# Verifica que el mock fue llamado con argumentos específicos.

# Si los argumentos no coinciden, el test falla.

from unittest.mock import Mock

m = Mock()
m.sumar(2, 3)

m.sumar.assert_called_with(2, 3)   # ✅ pasa
# m.sumar.assert_called_with(5, 5)   # ❌ AssertionError

############################################################################

# call
# Es un objeto que representa una llamada a un mock con ciertos argumentos.

# Se usa para construir listas de llamadas esperadas.

from unittest.mock import Mock, call

m = Mock()
m.enviar("hola")
m.enviar("chau")

print(m.mock_calls)
# → [call.enviar('hola'), call.enviar('chau')]

# Verificación explícita
esperadas = [call.enviar("hola"), call.enviar("chau")]
assert m.mock_calls == esperadas


############################################################################

# assert_has_calls
# Verifica que el mock recibió una secuencia de llamadas (en orden o no).

# Se usa junto con call.

from unittest.mock import Mock, call

m = Mock()
m.procesar(1)
m.procesar(2)
m.procesar(3)

# Verifica llamadas en orden
m.procesar.assert_has_calls([call(1), call(2), call(3)])

# Verifica llamadas sin importar orden
m.procesar.assert_has_calls([call(3), call(1)], any_order=True)

############################################################################

# En resumen

# Client.Connect es un atributo del mock.
# Si lo dejas sin paréntesis, es simplemente otro Mock (un objeto que representa el método).
# No registra ninguna llamada.

# Client.Connect() con paréntesis significa llamar al método.
# Esto sí registra la llamada en el historial (mock_calls).
# Es lo que necesitas si quieres comprobar que se invocó.

# assert_called_with y assert_has_calls: no devuelven nada útil 
# (solo validan, y si falla → AssertionError).

# call: sí devuelve un objeto que representa la llamada, 
# y se puede comparar con lo que ocurrió realmente.