import pytest

@pytest.mark.xfail(reason="Funcionalidad aún no implementada",strict=True)
class TestNuevaFeature:
    def test_crear(self):
        assert False

    def test_borrar(self):
        assert False
