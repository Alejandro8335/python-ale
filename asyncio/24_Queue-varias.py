import asyncio

async def productor(queues):
    # Genero 3 ítems y los mando a distintas colas
    for i, q in enumerate(queues, start=1):
        item = f"item-{i}"
        await q.put(item)
        print(f"Productor envió {item} a la cola {i}")
    # Señal de fin
    for q in queues:
        await q.put(None)

async def consumidor(nombre, queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"{nombre} procesó {item}")
        await asyncio.sleep(1)

async def main():
    # Creo 3 colas, una por consumidor
    q1, q2, q3 = asyncio.Queue(), asyncio.Queue(), asyncio.Queue()
    queues = [q1, q2, q3]

    await asyncio.gather(
        productor(queues),
        consumidor("Función A", q1),
        consumidor("Función B", q2),
        consumidor("Función C", q3),
    )

asyncio.run(main())

# 👉 El productor y el consumidor comparten el mismo objeto q. 
# Si crearas dos colas distintas (q1, q2), 
# cada consumidor tendría su propio canal y no vería lo que pasa en la otra.