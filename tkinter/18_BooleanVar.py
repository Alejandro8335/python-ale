import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplo BooleanVar")

bool = tk.BooleanVar(value=True)

check = tk.Checkbutton(ventana,text="accept",variable=bool)
check.pack()

etiqueta = tk.Label(ventana)
etiqueta.pack()

def Update(args):
    etiqueta.config(text=bool.get())#0 or 1
    print(bool.get())#True or False

bool.trace("w",Update)

ventana.mainloop()