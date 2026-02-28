# ¿Qué es patch?

# patch reemplaza temporalmente un atributo (función, clase, variable u objeto) dentro del namespace de un módulo durante el alcance del test.

# Cuando el test termina, el valor original se restaura automáticamente.

# 📌 Regla de oro:

# Patch where it is looked up, not where it is defined.

#========================================================================================================================
# modulo.__dict__["nombre"] = Mock()

#========================================================================================================================
from unittest.mock import patch

@patch("servicio.obtener_datos")
def test_funcion(mock_obtener):
    mock_obtener.return_value = {"ok": True}
    
    resultado = mock_obtener()
    
    assert resultado == {"ok": True}

# Qué pasó aquí:

# servicio.obtener_datos fue reemplazado por un Mock

# mock_obtener es ese Mock

# Cuando termina el test → se revierte automáticamente

#========================================================================================================================
# util cuando querés controlar el alcance manualmente:

from unittest.mock import patch

with patch("servicio.obtener_datos") as mock_obtener:
    mock_obtener.return_value = {"ok": True}
    print(mock_obtener())

# Sale del with → vuelve el original.

#========================================================================================================================
# Si el código a testear está en app.py:

# app.py
# from servicio import obtener_datos

# def ejecutar():
#     return obtener_datos()

# Entonces el patch correcto es:

# @patch("app.obtener_datos")

# Porque ejecutar() busca en el namespace de app.

#========================================================================================================================
# Se usa cuando ya tenés la referencia del objeto o clase.

# En vez de pasar una ruta como string, pasás el objeto directamente.

# Ejemplo con clase
from unittest.mock import patch

class Servicio:
    def obtener_datos(self):
        return {"real": True}

with patch.object(Servicio, "obtener_datos", return_value={"mock": True}):
    s = Servicio()
    print(s.obtener_datos())

# Salida:

{"mock": True}

#========================================================================================================================
# El orden de los mocks en decoradores

# El mock más cercano a la función es el primer parámetro.

@patch("modulo.A")
@patch("modulo.B")
def test(mock_B, mock_A):
    pass

# Se pasan en orden inverso.