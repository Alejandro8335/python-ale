import tkinter as tk
from tkinter.scrolledtext import ScrolledText

ventana = tk.Tk()
text = tk.Text(ventana,width=40 ,height=10,wrap="word",bg="grey",fg="black",padx=100,pady=10,font=("helventica",12))
text.pack()

text.insert("1.0","welcome to edit text")
text.insert("end","\n\nexample the text","resaltado")
text.tag_configure("resaltado",background="red",foreground="white")

content = text.get("1.0","end")
#text.delete("2.0","end")#borra el contenido,el numero son la linea de texto
print(content)

text_dezplasable = ScrolledText(ventana)
text_dezplasable.pack()         


ventana.mainloop()