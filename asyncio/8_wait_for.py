# ¿Qué hace?

# Ejecuta una corrutina o tarea, pero con un timeout máximo.

# Si la corrutina no termina en ese tiempo, se lanza una excepción asyncio.TimeoutError.

# Esto es muy útil cuando esperás respuestas de red, sensores, o cualquier operación que podría “colgarse”.

import asyncio

async def tarea_lenta():
    print("Empieza tarea lenta...")
    await asyncio.sleep(5)   # tarda 5 segundos
    print("Tarea lenta terminó")
    return "OK"

async def main():
    try:
        # Le damos máximo 3 segundos
        resultado = await asyncio.wait_for(tarea_lenta(), timeout=3)
        print("Resultado:", resultado)
    except asyncio.TimeoutError:
        print("⏰ La tarea tardó demasiado y fue cancelada")

asyncio.run(main())

# timeout
# wait() → coordina varias tareas, timeout devuelve lo que haya terminado y lo que no.

# wait_for() → controla una sola tarea, timeout lanza excepción y cancela.