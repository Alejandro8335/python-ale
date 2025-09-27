import asyncio

async def Fetch_data(x):
    if x == 2:
        raise ValueError("JAJAJAJA")
    await asyncio.sleep(x)
    return f"fetch completado en {x} segundos"

async def Main():  
    tasks = [asyncio.create_task(Fetch_data(i))for i in range(1,5)]
    
    for task in tasks:
        try:
            result = await task
            print(result)
        except Exception as e:
            print(e)
if __name__ == "__main__":
    print("inicio")
    asyncio.run(Main())