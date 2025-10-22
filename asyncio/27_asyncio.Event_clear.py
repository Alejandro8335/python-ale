import asyncio

async def main():
    evento = asyncio.Event()

    async def tarea():
        print("Esperando señal...")
        await evento.wait()
        print("Señal recibida")

    asyncio.create_task(tarea())
    await asyncio.sleep(1)
    evento.set()   # desbloquea
    await asyncio.sleep(1)
    evento.clear() # vuelve a bloquear para futuros wait
    print("Evento reseteado")

asyncio.run(main())

# 🎯 Cuándo usarlo
# Para coordinar inicio de varias tareas 
# (ej: no empezar a leer sensores hasta que el hardware esté listo).

# Para sincronizar fases en un pipeline 
# (ej: esperar a que termine la inicialización antes de procesar datos).

# Para señales globales (ej: “detener todos los consumidores cuando llegue el fin”).