import tkinter as tk
from tkinter import ttk
# ttk se importa aparte porque es un submódulo de tkinter

ventana = tk.Tk()
ventana.title("combobox")

combobox = ttk.Combobox(ventana, width=30, font=("arial",12,"bold"))
combobox.pack()

elementos = ["elemento 1","elemento 2","elemento 3"]
combobox["values"] = elementos

#eliminar un elemento
# elementos.remove("elemento 1")
# combobox["values"] = elementos

#cambiando un valor
# indice = 1
# nuevo_valor = "nuevo elemento"
# elementos[indice] = nuevo_valor
# combobox["values"] = elementos
#se puede simplificar

def Elemento_seleccionado(eventos):
    print(combobox.get())

combobox.bind("<<ComboboxSelected>>",Elemento_seleccionado)

def Click(args):
    print("Click")
    
combobox.bind("<Button-1>",Click)
ventana.mainloop()