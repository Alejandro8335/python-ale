import sys
import pytest

@pytest.mark.skipif(sys.platform == "win32", reason="No corre en Windows")
class TestSoloLinux:
    def test_archivos(self):
        assert True

    def test_permisos(self):
        assert True