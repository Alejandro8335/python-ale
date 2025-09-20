import tkinter as tk

ventana = tk.Tk()

ventana.geometry("400x400")

#creando el objeto
frame = tk.Frame(ventana)
frame.configure(width=100,height=100,bg ="#23a2b9",bd=5)#bd borde

frame1 = tk.Frame(frame)
frame1.configure(width=50,height=50,bg ="red",bd=5)

#lo añiade a la ventana,tmb define le orden en el que aparecen  
frame.pack()
frame1.pack()

#son frame con titulo
labelframe = tk.LabelFrame(ventana,text="hola",bg="yellow",padx=10,pady=10)
labelframe.configure(width=50,height=50)
labelframe.pack()
ventana.mainloop()