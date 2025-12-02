import pytest

@pytest.mark.skip(reason="Estos tests no aplican en Windows")
class TestWindowsOnly:
    def test_registro(self):
        assert False

    def test_servicios(self):
        assert True
