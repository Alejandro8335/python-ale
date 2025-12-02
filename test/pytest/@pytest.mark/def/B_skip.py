# test_skip.py
import pytest

@pytest.mark.skip(reason="Este test no aplica en este entorno")
def test_skip_example():
    # Este código nunca se ejecuta
    assert 1 + 1 == 3

# Sirve para saltar un test siempre, sin importar la condición.

# Se usa cuando un test no aplica en cierto contexto, o cuando todavía no está listo.

# Pytest lo reporta como “skipped” en la salida.