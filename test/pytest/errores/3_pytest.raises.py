# Qué hace: es un context manager que pasa la prueba solo si dentro del bloque se lanza la excepción indicada; 
# si no se lanza, la prueba falla

# Cuándo usar: cuando quieres validar comportamiento ante entradas inválidas o errores esperados.

import pytest

def dividir(a, b):
    return a / b

def test_division_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(1, 0)
        

# pytest.raises con match
# Qué valida: además del tipo de excepción, comprueba que el mensaje de error contenga un texto específico o 
# cumpla una expresión regular.

# Uso típico: cuando quieres asegurarte de que el error no solo es del tipo correcto, sino que el mensaje es el esperado.

with pytest.raises(ZeroDivisionError, match="division by zero"):
    dividir(1, 0)

# Sin match: valida solo el tipo de excepción.

# Con match: valida tipo de excepción + contenido del mensaje.