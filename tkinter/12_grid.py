import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplo grid")

label_1 = tk.Label(ventana,text="celda 0,0")
label_1.grid(row=0,column=0,padx=5,pady=5)#pad es la separacion en el eje 

label_2 = tk.Label(ventana,text="celda 0,1")
label_2.grid(row=0,column=1,padx=5,pady=5)

label_3 = tk.Label(ventana,text="celda 1,0")
label_3.grid(row=1,column=0,padx=5,pady=5)

label_4 = tk.Label(ventana,text="celda 1,1")
label_4.grid(row=1,column=1,padx=5,pady=5)

ventana.mainloop()