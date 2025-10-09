import tkinter as tk
from tkinter import filedialog 

ventana = tk.Tk()
# ocultando la ventana
ventana.withdraw()

# cuidado que borra el los archivos
file = filedialog.asksaveasfile(mode="w",defaultextension=".txt")
if file:
    file.write("hola mundo")
    file.close()