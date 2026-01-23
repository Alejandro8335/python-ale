# El método reset_mock() sirve para reiniciar el estado interno del mock, es decir:

# Borra el historial de llamadas (mock_calls, call_args, call_count).

# Resetea los atributos relacionados con las llamadas.

# Deja el mock "limpio", como si nunca hubiera sido usado.

from unittest.mock import Mock

# Creamos un mock
m = Mock()

# Lo usamos
m("hola")
print(m.called)        # True
print(m.call_count)    # 1

# Reiniciamos
m.reset_mock()

print(m.called)        # False
print(m.call_count)    # 0

# ☣️⚠️no limpia el side_effect⚠️☣️