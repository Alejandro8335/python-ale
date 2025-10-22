# ¿Qué hace?
# Te permite esperar a un conjunto de tareas con más control que gather.

# Podés decidir si querés esperar a que:

# todas terminen (return_when=asyncio.ALL_COMPLETED), o

# que termine la primera (return_when=asyncio.FIRST_COMPLETED), o

# que empiece a fallar/terminar la primera (FIRST_EXCEPTION).


# Devuelve dos conjuntos:

# done → tareas que ya terminaron.

# pending → tareas que todavía siguen corriendo.


import asyncio

async def tarea(nombre, segundos):
    print(f"{nombre} empieza")
    await asyncio.sleep(segundos)
    print(f"{nombre} terminó después de {segundos} seg")
    return nombre

async def main():
    # Creo varias tareas
    t1 = asyncio.create_task(tarea("Tarea 1", 2))
    t2 = asyncio.create_task(tarea("Tarea 2", 4))
    t3 = asyncio.create_task(tarea("Tarea 3", 6))
    
    # Espero hasta que termine la primera
    done, pending = await asyncio.wait(
        {t1, t2, t3}, 
        return_when=asyncio.FIRST_COMPLETED
    )# espera objetos tipo Task o Future
    
    # tmb puedo usar gather para agrupar tareas pero cuenta como una tarea
    print("\n--- Resultado parcial ---")
    for d in done:
        print("Terminó:", d.result())
    print("Pendientes:", [p.get_name() for p in pending])

    # Ahora espero al resto
    await asyncio.wait(pending) # vuelve a poner a hacer las tareas que quedaron pendientes

    print("\n--- Todas completadas ---")

asyncio.run(main())

# timeout
#    ↓