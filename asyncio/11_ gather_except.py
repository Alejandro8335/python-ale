# ¿Qué hace asyncio.gather()?
# Recibe varias corrutinas o tareas.

# Las ejecuta en paralelo dentro del event loop.

# Devuelve una lista con los resultados, en el mismo orden en que las pasaste 
# (no importa en qué orden terminaron).

# Si alguna falla, por defecto lanza la excepción y cancela las demás 
# (aunque esto se puede cambiar con return_exceptions=True).

import asyncio

async def Task(nombre,time):
    await asyncio.sleep(time)
    print(f"{nombre},time: {time}")
    return f"{nombre} OK"

async def Falla():
    await asyncio.sleep(1)
    raise ValueError("Error en la tarea")

async def Main():
    resultados = await asyncio.gather(
        Task("T1", 2),
        Falla(),
        Task("T2", 1),
        return_exceptions=True
    )# Si no ponés return_exceptions=True, la excepción cancela todo el gather.
    print("Resultados:", resultados)

asyncio.run(Main())