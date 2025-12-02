import pytest
import time
@pytest.mark.slow
def test_calculo_pesado():
    # Simula un cálculo que tarda mucho
    time.sleep(2)
    assert 2 + 2 == 4