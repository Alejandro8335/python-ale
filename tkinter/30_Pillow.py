import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title("PhotoImage")
label = tk.Label(ventana)

#para importar imagenes jpg
imagen_pil = Image.open(r"C:\Users\gabri\OneDrive\Desktop\ALE\python-ale\resumen_pygame\imagenes_extras\imagen1.jpg")
imagen_escalada = imagen_pil.resize((50,50))#en una tupla las dimenciones
imagen_rotada = imagen_escalada.rotate(45)#hay que pasarle un angulo,gira para la izquierda,quedan siempre en un cuadrado
imagen_tk = ImageTk.PhotoImage(imagen_rotada)

button = tk.Button(ventana,image=imagen_tk)
button.pack()

ventana.mainloop()