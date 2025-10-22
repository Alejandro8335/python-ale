# 🔧 ¿Qué hace?
# Devuelve el loop que está corriendo actualmente.

# Solo funciona dentro de una corrutina o tarea.

# Si lo llamás fuera de un contexto asíncrono, lanza un RuntimeError 
# (a diferencia de get_event_loop(), que antes creaba uno nuevo).

import asyncio

async def demo():
    loop = asyncio.get_running_loop()
    print("Loop actual:", loop)

asyncio.run(demo())