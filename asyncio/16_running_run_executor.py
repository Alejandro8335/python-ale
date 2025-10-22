import asyncio
import time

def bloqueante():
    time.sleep(2)
    return "Trabajo pesado terminado"

async def main():
    loop = asyncio.get_running_loop()
    resultado = await loop.run_in_executor(None, bloqueante)
    print(resultado)

asyncio.run(main())