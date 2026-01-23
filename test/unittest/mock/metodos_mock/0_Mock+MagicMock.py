from unittest.mock import Mock, MagicMock

# Mock simple

# Es la clase base para crear objetos simulados.

# No implementa métodos mágicos por defecto.

# Si intentas usar operaciones como len(mock), iter(mock), with mock: o acceder a mock[0], 
# obtendrás otro Mock vacío, pero no un comportamiento realista.

# Se usa cuando solo necesitas simular métodos/atributos explícitos.

m = Mock()
m.sumar.return_value = 10

print(m.sumar(5, 6))   # → 10
print(len(m))          # → <Mock name='mock.__len__()' id='...'>

####################################################################################

# MagicMock con métodos mágicos

# Hereda de Mock, pero añade implementaciones para los métodos mágicos 
# (__len__, __iter__, __getitem__, __enter__, __exit__, etc.).

# Esto lo hace más conveniente cuando quieres simular objetos que se comportan como listas, 
# diccionarios, context managers, etc.

# Ideal para tests donde necesitas que el mock se comporte como un objeto Python completo

mm = MagicMock()
mm.__len__.return_value = 42
mm.__getitem__.return_value = "hola"

print(len(mm))       # → 42
print(mm[0])         # → "hola"

# También funciona como context manager
with mm as recurso:
    recurso.accion.return_value = "ok"
    print(recurso.accion())   # → "ok"

####################################################################################
# Usa Mock si solo necesitas simular funciones o atributos simples.

# Usa MagicMock si tu objeto simulado debe comportarse como estructuras de Python 
# (listas, diccionarios, context managers, etc.).