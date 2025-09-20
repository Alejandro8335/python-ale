import tkinter as tk

ventana = tk.Tk()
ventana.title("menu")

menubutton = tk.Menubutton(ventana,text="archivo")
menubutton.pack()

menu = tk.Menu(menubutton)
menubutton.config(menu=menu) 

def Open():
    print("open")

menu.add_command(label="Open",command=Open)
menu.add_command(label="Close")
ventana.mainloop()