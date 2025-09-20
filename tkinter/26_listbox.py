import tkinter as tk

ventana = tk.Tk()
ventana.title("listbox")

listbox = tk.Listbox(ventana,width=30,height=10,fg="white",bg="black",font=("arial",12,"bold"))
                     #selectmode=tk.MULTIPLE / multiple para seleccionar varios elemento

listbox.insert(tk.END,"elemento 1")
listbox.insert(tk.END,"elemento 2")
listbox.insert(tk.END,"elemento 3")
listbox.insert(0,"elemento 4")
listbox.insert(2,"elemento 5")

listbox.delete(2)#borrar elementos

def Select(event):
    # indice = listbox.curselection()
    # elemento = listbox.get(indice)
    # print(elemento)
    print(f"seleccionado {listbox.get(listbox.curselection())}")

listbox.bind("<<ListboxSelect>>",Select)

listbox.pack()

ventana.mainloop()