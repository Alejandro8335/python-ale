from apple import Apples
import pytest

# pytest "C:\Users\gabri\OneDrive\Desktop\ALE\python-ale\proyectos\snake\test_apple.py"

def test_Apples__init__():
    with pytest.raises(ValueError):
        apples = Apples(0.5,3,None)
    with pytest.raises(ValueError):
        apples = Apples(1,2.5,None)
    with pytest.raises(ValueError):
        apples = Apples(1,2,None)
    apples = Apples(50,3,None)

def te_Apples_Create():
    apples = Apples(None)