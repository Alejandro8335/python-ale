import tkinter as tk

ventana = tk.Tk()
text = tk.Text(ventana)
text.pack()

def Copiar():
    text.event_generate("<<Copy>>")

def Cortar():
    text.event_generate("<<Cut>>")
    
def Pegar():
    text.event_generate("<<Paste>>")
    
button_copy = tk.Button(ventana,text="copiar",command=Copiar)
button_copy.pack()

button_cut = tk.Button(ventana,text="cortar",command=Cortar)
button_cut.pack()

button_paste = tk.Button(ventana,text="copiar",command=Pegar)
button_paste.pack()

ventana.mainloop()