# pytest "C:\Users\gabri\OneDrive\Desktop\ALE\python-ale\test\pytest\@pytest.mark\def\A_parametrize.py"
import pytest
def multiplicar(a,b):return a*b

@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 6),
    (5, 0, 0),
    (-4, 2, -8),
    (10, 10, 100),
])
def test_multiplicar(a, b, esperado):
    assert multiplicar(a, b) == esperado
# El decorador @pytest.mark.parametrize recibe dos cosas:
# Una cadena con los nombres de las variables: "a, b, esperado".
# Una lista de tuplas con los valores que se van a usar.

# pytest interpreta el decorador y genera varias ejecuciones del mismo test,
# una por cada tupla.

# En cada ejecución:
# Asigna los valores de la tupla a las variables (a, b, esperado).
# Llama a la función test_multiplicar con esos valores.