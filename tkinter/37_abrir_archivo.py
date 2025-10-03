import tkinter as tk
from tkinter import filedialog

def Open_file():
    file = filedialog.askopenfilename(filetypes=[("archivo de text","*.txt"),("todos los archivos","*.*")])
    if file:
        pass