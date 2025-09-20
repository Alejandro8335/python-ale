import tkinter as tk

def opcion_elegida():
    print("cambiado")

def habilitar():
    if variable_3.get():
        button.config(state="normal")
        
    else:
        button.config(state="disabled")
ventana = tk.Tk()
ventana.title("checkbutton")

variable_1 = tk.BooleanVar()

check_1 = tk.Checkbutton(ventana,text= "opcion 1",variable= variable_1,command= opcion_elegida)#mismo atributos que los button y radiobutton

check_1.pack()

variable_3 = tk.BooleanVar()
check_3 =  tk.Checkbutton(ventana,text= "opcion 3",variable= variable_3,command= habilitar)
button = tk.Button(ventana,text="tap",state="disabled",)

check_3.pack()
button.pack()

ventana.mainloop()