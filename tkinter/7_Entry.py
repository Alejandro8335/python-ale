import tkinter as tk

ventana = tk.Tk()
ventana.title("entry")

etiqueta = tk.Label(ventana)


entry = tk.Entry(ventana)
entry.config(fg="white",bg="black",font=("arial",12,"bold"))
#inserta un texto por defult
entry.insert(0,"text")
#guarda lo que hay escrito en esta variable
texto = entry.get()

def text():
    texto = entry.get()
    etiqueta.configure(text=texto)
    
button = tk.Button(ventana,text="tap",command=text)

etiqueta.pack()
entry.pack()
button.pack()
ventana.mainloop() 