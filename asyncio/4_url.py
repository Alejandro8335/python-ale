import asyncio

async def Download_data(url):
    print(f"descargando {url}")
    await asyncio.sleep(3)
    print(f"fin {url}")
    return f"data {url}"

async def Main():
    urls = ["http\\example.com\1","http\\example.com\2","http\\example.com\3"]
    tasks = [asyncio.create_task(Download_data(url))for url in urls]
    
    results = await asyncio.gather(*tasks)
    
    print("terminadas las tareas")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    print("inicio")
    asyncio.run(Main())