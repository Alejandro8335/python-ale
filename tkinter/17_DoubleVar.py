import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplo DoubleVar")

decimal = tk.DoubleVar(value=3.14)

control_deslizante = tk.Scale(ventana,variable=decimal,from_=0,to=10,resolution=0.01,
                              orient="horizontal")
control_deslizante.pack()

ventana.mainloop()