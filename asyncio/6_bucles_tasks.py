import asyncio

async def task(sleep,for_):
    for i in range(for_):
        await asyncio.sleep(sleep)
        print(f"Tarea ejecutada {sleep} segundos")

async def main():
    await asyncio.gather(
        task(1,5),
        task(2,5),
        task(3,5)
    )# No hace falta create_task porque gather lo hace por vos

asyncio.run(main())