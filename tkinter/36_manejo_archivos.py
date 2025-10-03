import tkinter as tk
from tkinter import filedialog

ventana = tk.Tk()
ventana.withdraw() # oculta la ventana principal

# haciendo que me abra el navegadot de archivos y me da la ruta del archivo
# file_path = filedialog.askopenfilename()

# si quiero abrir mas de un archivo y me da una lista de rutas
# file_path = filedialog.askopenfilenames()


# me abre el archivo 
file_read = filedialog.askopenfile(mode="r")# es de lectura

if file_read:
    print(file_read.read())
    file_read.close()
