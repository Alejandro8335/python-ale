import tkinter as tk 

ventana = tk.Tk()
text = tk.Text(ventana)

scrollbar_vertical  = tk.Scrollbar(ventana)
# No es obligatorio pasar ventana si solo tenés un Tk().(tmb pata Text)

# Es buena práctica siempre especificar el contenedor (ventana, frame, etc.),
# porque te da control y evita problemas cuando tu GUI crezca.

scrollbar_vertical.pack(side="right",fill= "y")
#side para ubicarla y fill define el eje

scrollbar_vertical.config(command=text.yview)
text.config(yscrollcommand=scrollbar_vertical.set)
text.pack(fill="both",expand=True)#side="right"
ventana.mainloop()