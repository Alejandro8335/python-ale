import asyncio

async def productor(queue):
    destinos = ["A", "B", "C"]
    for i, d in enumerate(destinos, start=1):
        item = f"item-{i}"
        await queue.put((d, item))
        print(f"Productor envió {item} para {d}")
    await queue.put((None, None))  # señal de fin
    
    for _ in range(3):
        await queue.put((None, None))

async def consumidor(nombre, queue):
    while True:
        destino, item = await queue.get()
        if destino is None:
            break
        if destino == nombre:
            print(f"Consumidor {nombre} procesó {item}")
            await asyncio.sleep(1)

async def main():
    q = asyncio.Queue()
    await asyncio.gather(
        productor(q),
        consumidor("A", q),
        consumidor("B", q),
        consumidor("C", q),
    )

asyncio.run(main())