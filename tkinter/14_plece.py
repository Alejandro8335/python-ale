import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplo plece")

# label_1 = tk.Label(ventana,text="label 1")
# label_1.place(x=50,y=50)

# label_2 = tk.Label(ventana,text="label 2")
# label_2.place(x=100,y=100)

#porcentaje en el eje
ventana.geometry("300x300")

label_1 = tk.Label(ventana,text="label 1")
label_1.place(relx=0.25,rely=0.25)

label_2 = tk.Label(ventana,text="label 2")
label_2.place(relx=0.75,rely=0.75)

ventana.mainloop()  