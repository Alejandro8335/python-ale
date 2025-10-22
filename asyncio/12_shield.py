# 🛡️ ¿Qué hace asyncio.shield()?
# Protege una corrutina o tarea de ser cancelada por quien la espera.

# Si el caller (el que hace await) se cancela, 
# la tarea protegida sigue corriendo en segundo plano.

# Sin shield, si cancelás el await, la tarea también se cancela.

import asyncio

async def tarea():
    try:
        print("Tarea empieza")
        await asyncio.sleep(5)
        print("Tarea terminó")
    except asyncio.CancelledError:
        print("Tarea fue cancelada")

async def main():
    t = asyncio.create_task(tarea())
    await asyncio.sleep(1)
    print("Cancelando el await...")
    try:
        # Protejo la tarea con shield
        await asyncio.wait_for(asyncio.shield(t), timeout=2)
    except asyncio.TimeoutError:
        print("El await fue cancelado, pero la tarea sigue viva")
    await asyncio.sleep(5)  # doy tiempo a que termine

asyncio.run(main())