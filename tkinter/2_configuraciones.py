import tkinter as tk

#creando un objeto
ventana = tk.Tk()#es una clase()TK

#cambiarle el tamaño
ventana.geometry("400x400")#ancho / largo

#definiendo el tamaño minimo
ventana.minsize(200,200)

#definiendo el tamaño maximo
ventana.maxsize(800,800)

#ponerle iconos
ventana.iconbitmap()#solo acepta archivos .ico

#cambiando el fondo
ventana.configure(bg="#23a2b9")#23a2b9

#bloqueando el tamaño 
ventana.resizable(True,False)

#cordenadas de aparicion
ventana.geometry("400x400+150+150")#x / y

#transparencia
ventana.attributes("-alpha",0.8)
#abriendo la ventana
ventana.mainloop()