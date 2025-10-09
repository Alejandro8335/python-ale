from tkinter import Tk , filedialog , Text ,Button , END , INSERT

def Open_file():
    global text
    file = filedialog.askopenfilename(filetypes=[("archivo de text","*.txt"),("todos los archivos","*.*")])
    if file:
        with open(file,"r") as file_obj:
            text.delete(1.0,END)
            text.insert(INSERT,file_obj.read())

def Save_file():
    global text
    file = filedialog.askopenfilename(filetypes=[("archivo de text","*.txt"),("todos los archivos","*.*")])
    if file:
        with open(file,"w") as file_obj:
            file_obj.write(text.get(1.0,END))

ventana = Tk()

text = Text(ventana,wrap="word")
text.pack(expand=True,fill="both")

open_button = Button(ventana,text="open file",command= Open_file)
open_button.pack(side="left")

save_button = Button(ventana,text="save file ",command=Save_file)
save_button.pack(side="right")

ventana.mainloop()