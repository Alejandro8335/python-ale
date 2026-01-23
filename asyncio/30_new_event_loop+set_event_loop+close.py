import asyncio

# asyncio.new_event_loop()

loop = asyncio.new_event_loop()

# ✔️ Crea un event loop nuevo
# ✔️ NO lo arranca
# ✔️ NO es global automáticamente
# 👉 Es solo un objeto en memoria.

asyncio.set_event_loop(loop)

# ✔️ Marca ese loop como:

# “el loop actual de ESTE hilo”

# 👉 Algunas APIs de asyncio lo buscan ahí.

loop1 = asyncio.new_event_loop()
asyncio.set_event_loop(loop1)

loop2 = asyncio.new_event_loop()
asyncio.set_event_loop(loop2)

# ¿Se rompen los loops?

# ❌ NO se rompen
# ✔️ Ambos existen en memoria

# ¿Cuál queda “activo”?

# 👉 El ÚLTIMO que seteás

# loop2 = loop actual del hilo

# loop1 = sigue existiendo, pero nadie lo usa

# ¿Qué pasa con las tareas?
# loop1.create_task(tarea1())
# loop2.create_task(tarea2())


# ✔️ Las tareas quedan atadas a su loop

loop.close()
loop1.close()
loop2.close()