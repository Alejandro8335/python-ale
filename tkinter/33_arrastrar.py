import tkinter as tk

def Arrastrar(event):
    global objecto_seleccionado
    objecto_seleccionado = canva.find_closest(event.x,event.y)[0]
    # El método devuelve el ID del objeto (o una tupla con el ID) que está más cerca de ese punto.
    # devuelve una tupla
def Soltar(event):
    global objecto_seleccionado
    if objecto_seleccionado:
        canva.move(objecto_seleccionado,event.x - canva.coords(objecto_seleccionado)[0],event.y - canva.coords(objecto_seleccionado)[1])
ventana = tk.Tk()
canva = tk.Canvas(ventana,width=500,height=500,bg= "white")
canva.pack(fill="both",expand= True)

objecto_seleccionado = None

canva.create_rectangle(100,100,200,200, fill="blue", tags="rectangle")

# cada vez que ocurra tal evento sobre este objeto con tal tag, ejecutá esta función

# canva.tag_bind("rectangle","<ButtonPress-1>",Arrastrar)
# canva.tag_bind("rectangle","<ButtonRelease-1>",Soltar)
# se dispara cuando soltás el botón izquierdo del mouse.

#esto hace que no tenga que seleccionar el rectagunlo si no que con tocar el canva 
#me selecciona al objeto mas cercano
canva.bind("<ButtonPress-1>",Arrastrar)
canva.bind("<ButtonRelease-1>",Soltar)

ventana.mainloop()