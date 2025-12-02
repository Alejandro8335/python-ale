# pytest "C:\Users\gabri\OneDrive\Desktop\ALE\python-ale\test\pytest\@pytest.mark\class\A_parametrize.py"
import pytest

class TestMath:
    @pytest.mark.parametrize("a,b,resultado", [
        (2, 3, 5),
        (10, -2, 8),
        (0, 0, 0),
    ])
    def test_suma(self, a, b, resultado):
        assert a + b == resultado
        
@pytest.mark.parametrize("valor", [1, 2, 3])
class TestMultiplicacion:
    def test_por_dos(self, valor):
        assert valor * 2 == valor + valor

    def test_por_tres(self, valor):
        assert valor * 3 == valor + valor + valor

# Si ponés @pytest.mark.parametrize en la clase, todos los métodos de test 
# dentro de esa clase reciben esos parámetros.