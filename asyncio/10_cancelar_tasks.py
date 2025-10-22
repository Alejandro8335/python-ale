# ¿Qué hace?
# Convierte una corrutina en una Task registrada en el event loop.

# La tarea empieza a ejecutarse en cuanto el loop tenga oportunidad (no inmediatamente en la línea).

# Te devuelve un objeto Task que podés:

# Esperar con await.

# Cancelar con .cancel().

# Consultar con .done(), .result(), .exception().

import asyncio

async def tarea():
    try:
        print("Tarea empieza")
        await asyncio.sleep(10)
        print("Tarea terminó")
    except asyncio.CancelledError:
        print("Tarea fue cancelada")

async def main():
    t = asyncio.create_task(tarea())
    await asyncio.sleep(2)
    print("Cancelando tarea...")
    t.cancel()
    await t  # importante: esperar para que se procese la cancelación

asyncio.run(main())