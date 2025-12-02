import pytest
import warnings

@pytest.mark.filterwarnings("error:.*deprecated.*")
class TestDeprecations:
    def test_funcion_vieja(self):
        warnings.warn("esta función está deprecated", DeprecationWarning)
        assert True

    def test_otro(self):
        warnings.warn("deprecated API", DeprecationWarning)
        assert True