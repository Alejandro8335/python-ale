# Mini resumen de protocol en Tkinter

# Función principal:  
# root.protocol("WM_DELETE_WINDOW", callback) 

# Sirve para capturar el evento cuando el usuario intenta cerrar la ventana (clic en la ❌).

# Eventos más usados:
# "WM_DELETE_WINDOW" → cuando se intenta cerrar la ventana.

import tkinter as tk

def on_closing():
    print("La ventana se está cerrando...")
    root.destroy()  # cerrar de forma controlada

root = tk.Tk()
root.title("Ejemplo protocol")

# Captura el evento de cierre
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
