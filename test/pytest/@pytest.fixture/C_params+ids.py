# Es un argumento de @pytest.fixture que permite que el fixture se ejecute varias 
# veces con distintos valores.

# Cada valor de la lista params se pasa al fixture a través de request.param.

# Resultado: el mismo test se corre múltiples veces, una por cada valor.
import pytest

@pytest.fixture(params=[1, 2, 3])
def numero(request):
    dato = request.param
    print(dato)
    return dato

def test_doble(numero):
    assert numero * 2 in [2, 4, 6]

@pytest.fixture(params=["admin", "usuario", "invitado"])
def rol(request):
    return {"rol": request.param}

def test_roles(rol):
    assert rol["rol"] in ["admin", "usuario", "invitado"]
    
#######################################################
@pytest.fixture(params=[0, 1], ids=["cero", "uno"])
def valor(request):
    return request.param
def test_valor(valor):
    assert valor in [0, 1]
