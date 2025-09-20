import tkinter as tk

root = tk.Tk()
root.title("menu")

def Menu_contextual(event):
    menu.tk_popup(event.x_root, event.y_root)
     
menu = tk.Menu(root,tearoff=0)
menu.add_command(label="cortar")
menu.add_command(label="copiar")
menu.add_command(label="pegar")

root.bind("<Button-3>",Menu_contextual)

entry = tk.Entry(root)
entry.pack()
root.mainloop()