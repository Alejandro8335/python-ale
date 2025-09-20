import time
import tkinter as tk

ventana = tk.Tk()
ventana.title("reloj")
etiqueta = tk.Label(ventana,text="hola")
etiqueta.pack()
def update_time():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    ventana.after(1000,update_time)#se ejecuta cada sierto tiempo

update_time()

ventana.mainloop()
