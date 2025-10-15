import asyncio

async def task(sleep,for_):
    for i in range(for_):
        await asyncio.sleep(sleep)
        print(f"Tarea ejecutada {sleep} segundos")

async def main():
    await asyncio.gather(
        asyncio.create_task(task(1,5)),
        asyncio.create_task(task(2,5)),
        asyncio.create_task(task(3,5))
    )

asyncio.run(main())