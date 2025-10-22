# ¿Qué hace?
# Recibe un conjunto de corrutinas o tareas.

# Devuelve un iterador asíncrono que va entregando las tareas en el orden en que se completan, no en el orden en que las pasaste.

# Te permite ir procesando resultados “en streaming”.

import asyncio
import random

async def tarea(nombre):
    segundos = random.randint(1, 5)
    print(f"{nombre} empieza (tardará {segundos}s)")
    await asyncio.sleep(segundos)
    return f"{nombre} terminó en {segundos}s"

async def main():
    tareas = [tarea(f"T{i}") for i in range(1, 4)]

    print("\nProcesando resultados a medida que llegan:\n")
    for fut in asyncio.as_completed(tareas):
        resultado = await fut
        print("Resultado recibido:", resultado)

asyncio.run(main())

# gather() → devuelve todos los resultados juntos, en el mismo orden en que pasaste las corrutinas.

# wait() → devuelve dos conjuntos (done, pending) y vos decidís qué hacer.

# as_completed() → te da un iterador para procesar resultados uno por uno, en cuanto estén listos.