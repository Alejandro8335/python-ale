import tkinter as tk

ventana = tk.Tk()#es una clase()TK
ventana.configure(bg="#23a2b9")
ventana.geometry("400x400+150+150")
ventana.attributes("-alpha",0.85)

etiqueta = tk.Label(ventana,text="hola soy label")
etiqueta.pack()

#sirve para configurara los objetos puede cambiar su estado 
etiqueta.config(fg="blue",bg="yellow",font=("arial",12,"bold"))
#bg es fondo y fg la letra
ventana.mainloop()

# Para leer el texto → label.cget("text").