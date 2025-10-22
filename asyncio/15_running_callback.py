import asyncio

def callback(msg):
    print("Callback ejecutado:", msg)

async def main():
    loop = asyncio.get_running_loop()
    loop.call_later(2, callback, "Hola desde el futuro")  # se ejecuta en 2s
    print("Esperando...")
    await asyncio.sleep(3)

asyncio.run(main())