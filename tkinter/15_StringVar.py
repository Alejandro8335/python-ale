import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplo StringVars")

stringvar = tk.StringVar(value="hola mundo")#puedo o no tener un value
stringvar.set("new text")

#print(text)
#print(text.get())

entrada = tk.Entry(ventana,textvariable=stringvar)
entrada.pack()

etiqueta = tk.Label(ventana)
etiqueta.pack()

def Update_Label(args):
    etiqueta.config(text=stringvar.get())

stringvar.trace("w",Update_Label)
ventana.mainloop()