import tkinter as tk
from tkcalendar import Calendar

ventana = tk.Tk()

cal = Calendar(ventana,selectmode= "day",locale="es_ES",year = 2025,month = 10,day=9,date_pattern="y-mm-dd")
cal.pack(expand=True,fill="both")

# Parámetro  /  Descripción:
# selectmode  /  "day" permite seleccionar días individuales. También puede ser "month" o "none".
# locale  /  "es_ES" muestra el calendario en español (nombres de meses, días, etc.).
# year, month, day  /  Fecha inicial que se muestra al abrir el calendario.
# date_pattern  /  Formato de fecha devuelto por get_date(). "y-mm-dd" → 2025-10-09.

cal.bind("<<CalendarSelected>>",lambda e:print(cal.get_date()))
ventana.mainloop()