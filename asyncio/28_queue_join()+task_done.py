# 📌 Conceptos clave
# En asyncio.Queue tenemos dos métodos importantes para coordinar tareas:

# task_done()  
# Se llama cuando una tarea que salió de la cola terminó su procesamiento.
# 👉 Sirve para avisar que ya se completó el trabajo asociado a un ítem.

# join()  
# Espera hasta que todos los ítems puestos en la cola hayan sido procesados (es decir, que se haya llamado a task_done() por cada uno).
# 👉 Es como decir: “no sigo hasta que todo lo que puse en la cola esté terminado”.

import asyncio

async def worker(queue, name):
    while True:
        item = await queue.get()
        print(f"{name} procesando {item}")
        await asyncio.sleep(1)  # simula trabajo
        queue.task_done()       # avisamos que terminamos
        print(f"{name} terminó {item}")

async def main():
    queue = asyncio.Queue()

    # lanzamos dos workers
    asyncio.create_task(worker(queue, "Worker-1"))
    asyncio.create_task(worker(queue, "Worker-2"))

    # ponemos tareas en la cola
    for i in range(5):
        await queue.put(i)

    print("Esperando que se procesen todas las tareas...")
    await queue.join()  # espera hasta que todas estén completadas
    print("¡Todas las tareas fueron procesadas!")

asyncio.run(main())

# Los workers sacan elementos de la cola y los procesan.

# Cada vez que terminan, llaman a task_done().

# El main espera con join() hasta que todos los ítems se procesen.