# 🔧 ¿Qué es un Semaphore?
# Un semáforo es un contador que limita cuántas tareas 
# pueden acceder a un recurso compartido al mismo tiempo.

# Imaginá que tenés 10 tareas que quieren hacer peticiones HTTP, 
# pero tu servidor solo permite 3 conexiones simultáneas.

# Con un Semaphore(3) asegurás que nunca haya más de 3 tareas ejecutándose 
# en paralelo dentro de la sección protegida.

import asyncio
import random

async def worker(nombre, sem):
    async with sem:  # 👈 solo N tareas entran a la vez
        print(f"{nombre} entra a la sección crítica")
        await asyncio.sleep(random.uniform(1, 3))
        print(f"{nombre} sale de la sección crítica")

async def main():
    sem = asyncio.Semaphore(3)  # máximo 3 tareas simultáneas
    tareas = [asyncio.create_task(worker(f"T{i}", sem)) for i in range(1, 11)]
    await asyncio.gather(*tareas)

asyncio.run(main())
