from tkinter import Tk,Button
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename,asksaveasfilename

ventana = Tk()
text = ScrolledText(ventana,wrap="word")#(word)salta línea por palabra completa. Evita cortar palabras a la mitad.
text.pack(expand=True,fill="both")#expand le dice que ocupe todo el espacio disponible
#both le dice en ambas direcciones

def Open_file():
    archivo = askopenfilename()
    if archivo:
        text.delete(1.0,"end")
        with open(archivo,"r") as file:
            text.insert(1.0,file.read())
            
def Guard_file():
    archivo = asksaveasfilename()
    if archivo:
        with open(archivo,"w") as file:
            file.write(text.get(1.0,"end"))

button_open = Button(ventana,text="open file",command=Open_file)
button_open.pack(side="left")

button_guard = Button(ventana,text="guard file",command=Guard_file)
button_guard.pack(side="left")

ventana.mainloop()
