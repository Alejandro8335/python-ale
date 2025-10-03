import tkinter as tk

ventana = tk.Tk()
ventana.title("listbox")

listbox = tk.Listbox(ventana,width=30,height=10,fg="white",bg="black",font=("arial",12,"bold"))

listbox.insert(tk.END,"elemento 1")
listbox.insert(tk.END,"elemento 2")
listbox.insert(tk.END,"elemento 3")

def Click(event):
    print("Click")

def Double_click(event):
    print("Double_click")
    
listbox.bind("<Button-1>",Click)
listbox.bind("<Double-Button-1>",Double_click)

listbox.pack()

ventana.mainloop()