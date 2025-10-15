import tkinter as tk
from tkinter import filedialog
import os
from tkinter import messagebox

# Funciones para las opciones de archivo
file_route = None

def new_file():
    global texto,label_file
    texto.delete(1.0, tk.END)
    label_file.config(text="")

def open_file():
    global texto,file_route,label_file
    file_route = filedialog.askopenfilename(filetypes=[("Python y Texto",("*.py","*.txt")),("Solo Texto","*.txt"),("Solo Python","*.py"),("Todos los archivos","*.*")])
    if file_route:
        with open(file_route,"r",encoding="utf-8") as file:
            texto.delete(1.0,tk.END)
            texto.insert(1.0,file.read())
            label_file.config(text=os.path.basename(file_route))
        
def save_file():
    global file_route,texto
    if file_route:
        try:
            with open(file_route,"w",encoding="utf-8") as file:
                file.write(texto.get(1.0,tk.END))
                messagebox.showinfo("Guardado", "El archivo se guardó correctamente.")
        except:
            messagebox.showerror("Error de Guardado", "El archivo se no guardó correctamente.")
            


def save_as_file():
    global texto
    save_route = filedialog.asksaveasfilename(filetypes=[("Python y Texto",("*.py","*.txt")),("Solo Texto","*.txt"),("Solo Python","*.py"),("Todos los archivos","*.*")])
    if save_route:
        try:
            with open(save_route,"w",encoding="utf-8") as file:
                file.write(texto.get(1.0,tk.END))
                messagebox.showinfo("Guardado", "El archivo se guardó correctamente.")
        except:
            messagebox.showerror("Error de Guardado", "El archivo se no guardó correctamente.")
            
# Funciones para las opciones de editar
def copy():
    texto.event_generate("<<Copy>>")

def paste():
    texto.event_generate("<<Paste>>")

def cut():
    texto.event_generate("<<Cut>>")

# configuraciones de la ventana
ventana = tk.Tk()
ventana.title("Bloc de Notas")
ventana.geometry("600x400")
ventana.configure(bg="#085967")

# label
label_file = tk.Label(ventana,bg="#19414A",anchor="w",fg="#FFFFFF")
label_file.pack(expand=True,fill="both")

# creando el area de menus
menu = tk.Menu(ventana)
ventana.config(menu=menu)

# menu de archivos
files = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=files)

for label,command in [("Nuevo",new_file),("Abrir",open_file),("Guardar",save_file),("Guardar como",save_as_file)]:
    files.add_command(label=label,command=command)

# menu de editar
edit = tk.Menu(menu)
menu.add_cascade(label="Editar", menu=edit)

for label,command in [("Copiar", copy), ("Pegar", paste), ("Cortar", cut)]:
    edit.add_command(label=label, command=command)

# area de texto
texto = tk.Text(ventana,font=("Arial", 14), bg="#122E34",fg="#FFFFFF",insertbackground="#FFFFFF")
texto.pack(expand=True, fill='both')
ventana.mainloop()