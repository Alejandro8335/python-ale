import tkinter as tk

ventana = tk.Tk()
canva = tk.Canvas(ventana,width=500,height=500,bg= "white")

canva.create_rectangle(50,50,150,100,fill="green",outline="black",width=2,tags="rectangulo")

# los 4 primeros números son dos pares de coordenadas (x, y) que marcan las vertices opuestos del rectángulo que 
# define el tamaño y la posición del óvalo.

# las dos primeras cordenadas marcan dos vertices y los otros dos se generan solos pq tiene que estar a 90 grados

# La tag no se muestra en pantalla, es solo un identificador.

# Podés usarla para configurar, mover o enlazar eventos a los 
# objetos que tengan esa etiqueta.

#sirve para mover formas
canva.move("rectangulo",100,100)

canva.create_oval(175,25,275,125,fill="blue",outline="black",width=3)
# ouline define el color del borde(si no esta no tiene borde),width define el ancho del borde

# las cordenadas del ovalo funcionan como las del rectagulo

canva.create_polygon(250,225,350,325,250,325,350,425,fill="blue",outline="black",width=3)
# 3 pares de  cordenas que definen sus vertices
# triangulo rectangulo(250,225,350,325,250,325)

canva.create_line(25,25,100,75,fill="orange",width=10,dash=(5,2),capstyle="butt")
# dash para hacer lines puntiadas

# capstyle:
# BUTT (por defecto) → el extremo termina justo en la coordenada final, plano.

# PROJECTING → el extremo sobresale un poco más allá de la coordenada final, como un rectángulo.

# ROUND → el extremo es redondeado, como un semicírculo.
canva.pack()
ventana.mainloop()