# 🔧 ¿Qué es un executor?
# Es un pool de hilos (ThreadPoolExecutor) o 
# procesos (ProcessPoolExecutor) que ejecuta funciones normales (sin await) en paralelo.

# asyncio.run_in_executor() manda esa función bloqueante al executor y 
# devuelve un futuro asíncrono que podés await.

import asyncio
import time

def funcion_bloqueante(nombre, segundos):
    print(f"{nombre} empieza (bloquea {segundos}s)")
    time.sleep(segundos)  # 👈 bloqueante
    print(f"{nombre} terminó")
    return f"{nombre} -> {segundos}s"

async def main():
    loop = asyncio.get_running_loop()

    # Ejecuto en un thread pool (por defecto)
    futuro1 = loop.run_in_executor(None, funcion_bloqueante, "T1", 3)
    futuro2 = loop.run_in_executor(None, funcion_bloqueante, "T2", 2)

    print("Mientras tanto, el loop sigue libre...")
    resultados = await asyncio.gather(futuro1, futuro2)
    print("Resultados:", resultados)

asyncio.run(main())

# executor=None → usa el ThreadPoolExecutor por defecto.

# Podés pasar tu propio ThreadPoolExecutor o ProcessPoolExecutor si querés más control.

# func, *args → la función normal (no async) y sus argumentos.