# 🔧 ¿Qué es un Lock?
# Un lock (candado) es la forma más estricta de exclusión mutua:

# Solo una tarea a la vez puede entrar en la sección protegida.

# Si otra tarea intenta entrar mientras el lock está ocupado, 
# queda esperando hasta que se libere.

# Es básicamente un Semaphore(1).

import asyncio
import random

async def worker(nombre, lock):
    async with lock:  # 👈 solo una tarea a la vez
        print(f"{nombre} entra a la sección crítica")
        await asyncio.sleep(random.uniform(1, 3))
        print(f"{nombre} sale de la sección crítica")

async def main():
    lock = asyncio.Lock()
    tareas = [asyncio.create_task(worker(f"T{i}", lock)) for i in range(1, 4)]
    await asyncio.gather(*tareas)

asyncio.run(main())

# Para proteger recursos compartidos que no toleran acceso concurrente 
# (ej: escribir en un archivo, actualizar una variable global, acceder a hardware).

# Para garantizar consistencia en operaciones críticas.