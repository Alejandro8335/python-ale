import pytest
# expected to fail
@pytest.mark.xfail(reason="Funcionalidad no implementada aún")
def test_xfail_example():
    # Este test va a fallar, pero pytest lo reporta como xfail
    assert 2 * 2 == 5
# Si el test pasa, pytest lo marca como XPASS (pasa inesperadamente).
@pytest.mark.xfail()
def test_xpass_example():
    assert 2*2 == 4

# Falla, se reporta como XFAIL
@pytest.mark.xfail(reason="Bug conocido", strict=True)# hace que sea estricto si XPASS entoces manda FAILED
def test_strict_falla():
    assert 1 + 1 == 3

# Pasa, se reporta como XPASS y ERROR
@pytest.mark.xfail(reason="Bug conocido", strict=True)
def test_strict_arreglado():
    assert 1 + 1 == 2

# Es útil cuando:
    # Hay un bug conocido que todavía no se corrigió.

    # Una funcionalidad aún no está implementada.

    # Querés que el reporte muestre claramente que ese fallo es esperado, 
    # no un error nuevo.