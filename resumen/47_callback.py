# Definimos una función callback
def mi_callback():
    print("Callback ejecutada.")

# Definimos una función que recibe otra función como parámetro
def ejecutar_con_callback(callback):
    print("Ejecutando tarea principal...")
    callback()  # aquí se llama a la función pasada

# Usamos la función
ejecutar_con_callback(mi_callback)

#Callback genérica: se usa para ejecutar lógica después de otra función.