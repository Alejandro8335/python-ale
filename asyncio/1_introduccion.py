import asyncio

async def Say_hello():
    print("hello")
    await asyncio.sleep(1)
    print("word")
    
if __name__ == "__main__":
    print("inicio")
    asyncio.run(Say_hello())