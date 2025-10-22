# 🔧 ¿Qué es un Event?
# Es como una bandera que puede estar en dos estados:

# No está puesta (clear) → las tareas que esperan el evento se bloquean.

# Está puesta (set) → todas las tareas que estaban esperando se desbloquean.

# Una vez que el evento está en estado set, cualquier tarea que haga await event.wait() 
# pasa inmediatamente.

# 👉 Es ideal para sincronizar: “no empieces hasta que yo te dé la señal”.

import asyncio

async def trabajador(nombre, evento):
    print(f"{nombre} esperando la señal...")
    await evento.wait()  # se bloquea hasta que el evento esté en set
    print(f"{nombre} recibió la señal y empieza a trabajar")

async def main():
    evento = asyncio.Event()

    # lanzo dos tareas que esperan la señal
    t1 = asyncio.create_task(trabajador("T1", evento))
    t2 = asyncio.create_task(trabajador("T2", evento))

    await asyncio.sleep(2)
    print("¡Señal enviada!")
    evento.set()  # desbloquea a todos los que estaban esperando

    await asyncio.gather(t1, t2)

asyncio.run(main())

# ⚙️ Métodos principales
# event.set() → activa la señal (desbloquea a todos los que esperan).

# event.clear() → vuelve a poner la señal en estado “apagado”.

# event.is_set() → consulta si la señal está activa.

# await event.wait() → espera hasta que la señal esté activa.