# mock_open

# Crea un mock que imita el comportamiento de open().

# Permite simular lectura y escritura de archivos en memoria.

# Se usa junto con patch para reemplazar la función open en el módulo que estás probando.

############################################################################
# simular lectura
from unittest.mock import mock_open, patch

# Contenido simulado del archivo
contenido = "línea1\nlínea2\n"

# Parcheamos open en el módulo donde se usa
with patch("builtins.open", mock_open(read_data=contenido)) as m:
    with open("archivo.txt") as f:
        datos = f.read()
        print(datos)   # → "línea1\nlínea2\n"

# Verificar que se llamó correctamente
m.assert_called_with("archivo.txt")
