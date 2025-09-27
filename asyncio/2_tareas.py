import asyncio

async def Task_1():
    await asyncio.sleep(2)
    print("task 1")
    
async def Task_2():
    await asyncio.sleep(1)
    print("task 2")
    
async def Main():
    task_1 = asyncio.create_task(Task_1())
    task_2 = asyncio.create_task(Task_2())
    
    await task_1
    await task_2

if __name__ == "__main__":
    print("inicio")
    asyncio.run(Main())