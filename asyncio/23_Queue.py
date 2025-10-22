# 🔧 ¿Qué es un Queue?
# Es una cola FIFO (primero en entrar, primero en salir).

# Una tarea puede poner datos (await queue.put(item)) y 
# otra puede sacarlos (item = await queue.get()).

# Maneja automáticamente la sincronización: si la cola está vacía, el consumidor espera; 
# si está llena (con maxsize), el productor espera.

import asyncio
import random

async def productor(queue):
    for i in range(3):
        await asyncio.sleep(random.uniform(0.5, 1.5))  # simula trabajo
        item = f"item-{i}"
        await queue.put(item)
        print(f"Productor generó: {item}")
    await queue.put(None)  # señal de fin

async def consumidor(queue):
    while True:
        item = await queue.get()
        if item is None:  # señal de fin
            break
        print(f"Consumidor procesó: {item}")
        await asyncio.sleep(1)  # simula procesamiento

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(
        productor(queue),
        consumidor(queue)
    )

asyncio.run(main())