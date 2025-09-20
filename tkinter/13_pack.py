import tkinter as tk

ventana = tk.Tk()
ventana.title("ejemplo pack")

frame_button = tk.Frame(ventana)
frame_button.pack(pady=10)

button_1 = tk.Button(frame_button,text="button 1")
button_1.pack(side= "left",padx=5)#buttom=abajo / left=izquierda / right=derecha / top=arriba

button_2 = tk.Button(frame_button,text="button 2")
button_2.pack(side= "left",padx=5)

button_3 = tk.Button(frame_button,text="button 3")
button_3.pack(side= "left",padx=5)

button_4 = tk.Button(frame_button,text="button 4")
button_4.pack(side= "left",padx=5)

ventana.mainloop()

#text.pack(expand=True,fill="both")
#expand le dice que ocupe todo el espacio disponible
#both le dice en ambas direcciones