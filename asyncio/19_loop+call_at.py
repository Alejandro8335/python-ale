# 🔧 Sintaxis
# python
# loop.call_at(when, callback, *args)
# when → instante absoluto en el reloj del loop (loop.time() te da el tiempo actual del loop).

# callback → función normal (no async).

# *args → argumentos opcionales para la función.

import asyncio

def callback(msg):
    print("Callback ejecutado:", msg)

async def main():
    loop = asyncio.get_running_loop()
    ahora = loop.time()
    print("Tiempo actual del loop:", ahora)

    # Programo un callback para dentro de 3 segundos,
    # pero usando call_at en lugar de call_later
    when = ahora + 3
    loop.call_at(when, callback, "Hola desde call_at")

    print("Esperando...")
    await asyncio.sleep(5)

asyncio.run(main())

# loop.time() devuelve un número flotante 
# (segundos desde que arrancó el loop, no la hora del sistema).

# call_at(ahora + 3, ...) es equivalente a call_later(3, ...).

# La diferencia es que con call_at podés programar eventos en tiempos absolutos, 
# útil si querés coordinar varias acciones con precisión.