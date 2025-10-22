import asyncio

async def Say_hello():
    print("hello")
    await asyncio.sleep(1)# Suspende la corrutina actual durante un tiempo sin bloquear el event loop.
    # await es lo que cede el control al loop, permitiendo que otras tareas empiecen o continúen.
    print("word")
    
if __name__ == "__main__":
    print("inicio")
    asyncio.run(Say_hello())