from unittest.mock import Mock

# Creamos un mock
mi_mock = Mock()

# Podemos definir qué devuelve cuando se llama
mi_mock.return_value = "Hola desde el mock"

# Usarlo como si fuera una función
print(mi_mock())   # → Hola desde el mock

# También podemos simular atributos
mi_mock.nombre = "Alejandro"
print(mi_mock.nombre)  # → Alejandro

# Y verificar si fue llamado
mi_mock()
print(mi_mock.called)  # → True
