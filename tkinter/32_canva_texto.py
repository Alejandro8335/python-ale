import tkinter as tk

ventana = tk.Tk()
canvas = tk.Canvas(ventana,width=500,height=500,bg= "white")
canvas.pack(fill="both",expand= True)

canvas.create_text(65,25,text="hola mundo",fill="darkgreen",font=("Courier",12,"italic"),justify="center")

ventana.mainloop()