import asyncio

async def Computer_square(x,t = 1):
    await asyncio.sleep(t)
    return x*x
    
    
async def Main():
    #tiempo 15 la suma de todas las tareas,se ejecuta de manera sincrona
    
    # result_0 = await Computer_square(1,2)
    # print("1 task")
    # result_1 = await Computer_square(2,1)
    # print("2 task")
    # result_2 = await Computer_square(3,3)
    # print("3 task")
    # result_3 = await Computer_square(4,5)
    # print("4 task")
    # result_4 = await Computer_square(5,4)
    # print("5 task")

    #tiempo 5 que es la mas lenta
    result = await asyncio.gather(
    Computer_square(1,2),Computer_square(2,1),
    Computer_square(3,3),Computer_square(4,5),
    Computer_square(5,4)
    )
    
    print(result)
    

if __name__ == "__main__":
    print("inicio")
    asyncio.run(Main())
