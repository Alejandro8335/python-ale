# Definimos un handler para un "evento"
def on_evento(mensaje):
    print(f"Handler recibió: {mensaje}")

# Simulamos una función que dispara un evento
def disparar_evento(handler):
    print("Evento ocurrido")
    handler("Hola desde el evento")

# Usamos el handler
disparar_evento(on_evento)

# Handler: se usa para reaccionar a un evento específico (clic, mensaje, interrupción).