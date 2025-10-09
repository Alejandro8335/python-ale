import tkinter as tk
from tkinter import filedialog

def Open_file():
    global text
    file = filedialog.askopenfilename(filetypes=[("archivo de text","*.txt"),("todos los archivos","*.*")])
    if file:
        with open(file,"r") as file_obj:
            text.delete(1.0,tk.END)
            text.insert(tk.INSERT,file_obj.read())
            
ventana = tk.Tk()

text = tk.Text(ventana,wrap="word")
text.pack(expand=True,fill="both")

open_button = tk.Button(ventana,text="open file",command=Open_file)
open_button.pack()

ventana.mainloop()