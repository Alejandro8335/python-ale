import tkinter as tk

ventana = tk.Tk()
ventana.title("menu")

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_main = tk.Menu(barra_menu)
barra_menu.add_cascade(label="main",menu=menu_main)

menu_main.add_command(label="new")
menu_main.add_command(label="open")
menu_main.add_separator()
menu_main.add_command(label="close")

#new menu
menu_edit = tk.Menu(barra_menu)
barra_menu.add_cascade(label="edit",menu=menu_edit)

menu_edit.add_command(label="undo")
menu_edit.add_separator()
menu_edit.add_command(label="redo")
ventana.mainloop()