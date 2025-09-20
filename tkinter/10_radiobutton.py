import tkinter as tk

ventana = tk.Tk()
ventana.title("radiobutton")

#opcion_1 = tk.Radiobutton(ventana,text="opcion 1")
#opcion_1.pack()

#variable_control = tk.IntVar()

#def mostrar():
    #print(variable_control.get())#buestra la valor de la opcion
    
def color_ventana():
    value = variable_control.get()
    if value == 2:
        ventana.config(bg="black")
    else:
        ventana.config(bg="white")
        
opcion_2 = tk.Radiobutton(ventana,text="black",value=2,command=color_ventana)
opcion_3 = tk.Radiobutton(ventana,text="white",value=3,command=color_ventana)

opcion_2.pack()
opcion_3.pack()
ventana.mainloop()