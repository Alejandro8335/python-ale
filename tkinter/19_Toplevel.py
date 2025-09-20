import tkinter as tk

ventana = tk.Tk()
ventana.title("main")
#ventana.geometry("400x400")

# toplevel = tk.Toplevel(ventana)
# toplevel.title("Toplevel")
# toplevel.geometry("300x200+50+50")

def Open_toplevel():
    toplevel = tk.Toplevel(ventana)
    toplevel.title("Toplevel")
    toplevel.geometry("300x200+50+50")
    etiqueta = tk.Label(toplevel,text="toplevel")
    etiqueta.pack()

def Close():
    ventana.destroy()
    
button_open = tk.Button(ventana,text="open toplevel",command=Open_toplevel) 
button_open.pack()

button_close = tk.Button(ventana,text="close",command=Close)
button_close.pack()
ventana.mainloop()