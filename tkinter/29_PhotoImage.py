import tkinter as tk

ventana = tk.Tk()
ventana.title("PhotoImage")

imagen = tk.PhotoImage(file=r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ALE\\resumen_pygame\\introducción\\items\\corazon_vacio.png")
imagen_2 = tk.PhotoImage(file=r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ALE\\resumen_pygame\\introducción\\items\\corazon_medio.png")

label = tk.Label(ventana,image=imagen)
button = tk.Button(ventana,image=imagen_2)
label.pack()
button.pack()

ventana.mainloop()