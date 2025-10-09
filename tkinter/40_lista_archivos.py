import tkinter as tk
from tkinter import filedialog 
import os

# os es como un puente entre Python y tu sistema operativo}

def seleccionar_directorio():
    dir = filedialog.askdirectory()
    if dir:
        list_box.delete(0,tk.END)
        for file in os.listdir(dir):
            list_box.insert(tk.END,file) 
            
ventana = tk.Tk()

list_box = tk.Listbox(ventana)
list_box.pack(expand=True,fill="both")

button = tk.Button(ventana,text="seleccionar",command=seleccionar_directorio)
button.pack()

ventana.mainloop()