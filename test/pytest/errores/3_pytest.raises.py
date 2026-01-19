# Qué hace: es un context manager que pasa la prueba solo si dentro del bloque se lanza la excepción indicada; 
# si no se lanza, la prueba falla

# Cuándo usar: cuando quieres validar comportamiento ante entradas inválidas o errores esperados.

import pytest

def dividir(a, b):
    return a / b

def test_division_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(1, 0)