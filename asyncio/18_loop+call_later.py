import asyncio

def callback(msg):
    print("Callback ejecutado:", msg)

async def main():
    loop = asyncio.get_running_loop()
    print("Programando callback dentro de 3 segundos...")
    loop.call_later(3, callback, "Hola desde call_later")# siempre tiene que haber tiempo pero puede ser 0
    await asyncio.sleep(5)  # espero lo suficiente para que se dispare

asyncio.run(main())

# 👉 call_later(segundos, funcion, *args) 
# agenda la función para que se ejecute después de ese tiempo. 

# 👉 Importante: la función que se ejecuta es normal (no async). 
# Si necesitás correr algo async, 
# lo habitual es que esa función cree una tarea con loop.create_task(...).