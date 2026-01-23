import asyncio

async def mi_corutina():
    return "resultado de la corutina"

async def main():
    # Creo la tarea
    tarea = asyncio.create_task(mi_corutina())

    # Más adelante, espero el resultado
    resultado = await tarea
    print(resultado)  # "resultado de la corutina"

asyncio.run(main())
# tmb se puede usar wait_for