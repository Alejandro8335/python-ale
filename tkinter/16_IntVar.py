import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplo IntVar")

intvar = tk.IntVar(value=42)

#print(IntVar.get())

# opcion_1 = tk.Radiobutton(ventana,text= "opcion 1",variable=intvar,onvalue= 1,offvalue=2)
# opcion_1.pack()

# opcion_2 = tk.Radiobutton(ventana,text= "opcion 2",variable=intvar,value=2)
# opcion_2.pack()

opcion_1 = tk.Checkbutton(ventana,text= "opcion 1",variable=intvar,onvalue= 0,offvalue=1)
opcion_1.pack()

etiqueta = tk.Label(ventana)
etiqueta.pack()

def Update(*args):
    etiqueta.config(text=intvar.get())
    
intvar.trace("w",Update)

print("e")

ventana.mainloop()