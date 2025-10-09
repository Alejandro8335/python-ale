import tkinter as tk
from tkcalendar import DateEntry

ventana = tk.Tk()
ventana.geometry("300x150")


date_entry = DateEntry(ventana,locale="es_ES",date_pattern="y-mm-dd",year=2025,month=10,day=9)
date_entry.pack()

label = tk.Label(ventana,text="selecciona una fecha")
label.pack()

def updata_date(event):
    label.config(text=f"fecha seleccionada: {date_entry.get_date()}")

date_entry.bind("<<DateEntrySelected>>",updata_date)

ventana.mainloop()