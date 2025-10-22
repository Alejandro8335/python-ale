import asyncio

async def worker(nombre, segundos):
    print(f"{nombre} empieza")
    await asyncio.sleep(segundos)
    print(f"{nombre} terminó")
    return f"{nombre} -> {segundos}s"

async def main():
    loop = asyncio.get_running_loop()   # obtengo el loop actual

    # Creo tareas dinámicamente usando el loop
    t1 = loop.create_task(worker("T1", 2))
    t2 = loop.create_task(worker("T2", 3))
    t3 = loop.create_task(worker("T3", 1))

    print("Tareas lanzadas, sigo con otras cosas...")

    # Espero a todas con gather
    resultados = await asyncio.gather(t1, t2, t3)
    print("Resultados:", resultados)

asyncio.run(main())

# Usamos loop.create_task(...) en lugar de asyncio.create_task(...).

# Ambas formas son equivalentes, pero con get_running_loop() 
# tenés acceso directo al loop y podés usar otros métodos avanzados 
# (call_later, run_in_executor, etc.).

# Las tareas se ejecutan en paralelo y 
# gather devuelve los resultados en el mismo orden en que las pasaste.