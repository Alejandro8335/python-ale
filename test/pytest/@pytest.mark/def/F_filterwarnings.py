import pytest
import warnings
# La llamada warnings.warn(...) genera una advertencia en tiempo de ejecución. 
# El primer argumento es el mensaje que verá el usuario; 
# el segundo es la clase de advertencia (aquí UserWarning) que clasifica el 
# tipo de aviso. Las advertencias se usan para señalar condiciones que merecen 
# atención pero que no justifican lanzar una excepción y terminar el programa


# Clase de Warning	    Cuándo aparece
# DeprecationWarning	Cuando se usa una función, clase o parámetro que está obsoleto y se planea eliminar en futuras versiones.
# UserWarning	        Cuando el propio código o una librería quiere emitir un aviso personalizado al usuario.
# RuntimeWarning        Cuando ocurre algo sospechoso en tiempo de ejecución, pero no lo suficientemente grave para ser excepción.
## Uso típico ##
# Avisar al programador que debe migrar a una alternativa nueva.
# Mensajes generales definidos por el desarrollador.
# Ejemplo: operaciones numéricas que pierden precisión, overflow silencioso, etc.

def test_warning():
    warnings.warn("Este es un warning de prueba", UserWarning)# Advertencia de usuario
@pytest.mark.filterwarnings("ignore:Este es un warning de prueba")
def test_ignore_warning():
    warnings.warn("Este es un warning de prueba", UserWarning)
    
@pytest.mark.filterwarnings("error:.*deprecated.*")
def test_deprecated():
    warnings.warn("Función deprecated", DeprecationWarning)# Advertencia de desuso
    # Esto va a fallar porque el warning se convierte en error

# Acción	Qué hace
# ignore	No muestra el warning, lo descarta.
# default	Muestra el warning la primera vez que aparece en cada ubicación.
# always	Muestra el warning siempre, aunque se repita.
# error	    Convierte el warning en una excepción (el test falla).
# module	Muestra el warning la primera vez que aparece en cada módulo.
# once	    Muestra el warning solo la primera vez que aparece en toda la ejecución.