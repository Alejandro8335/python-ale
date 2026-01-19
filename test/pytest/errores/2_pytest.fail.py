# Qué hace: marca la prueba como fallida inmediatamente con el mensaje que le pases; 
# es útil para condiciones que detectas en tiempo de test y quieres reportar explícitamente

# Cuándo usar: validaciones complejas, ramas que no deberían ejecutarse, o dentro de fixtures cuando quieres 
# abortar con razón clara.

import pytest

def test_condicion():
    precondicion = False
    if not precondicion:
        pytest.fail("Precondición no cumplida")
