import pytest
import sys

@pytest.mark.skipif(sys.version_info < (3, 10), reason="Requiere Python 3.10 o superior")
# si es True se salta
def test_requires_python310():
    # Algún código que usa sintaxis nueva
    assert (a := 5) == 5