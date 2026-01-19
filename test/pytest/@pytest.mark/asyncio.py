# Qué hace @pytest.mark.asyncio

# Le dice a pytest que el test es una coroutine (async def).

# Permite que pytest ejecute ese test dentro de un loop de asyncio.

############################################################################

# Cuándo lo necesitas

# Sí lo necesitas si tu test es async def y dentro usás await 
# (por ejemplo, await some_async_function() o await asyncio.create_task(...)).

# No lo necesitas si tu test es def normal y lo que probás es una función que 
# internamente crea tareas, pero vos no usás await en el test.

############################################################################
# donde hace falta
import pytest
import asyncio

@pytest.mark.asyncio
async def test_async_func():
    task = asyncio.create_task(asyncio.sleep(0.1))
    await task
    assert task.done()
    
############################################################################
# donde no hace falta
def test_sync_func():
    result = "funcion_que_crea_tareas()"
    assert result == "funcion_que_crea_tareas()"
