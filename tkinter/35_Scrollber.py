import tkinter as tk 

ventana = tk.Tk()
text = tk.Text(ventana)

scrollbar_horizontal  = tk.Scrollbar(ventana,orient=tk.HORIZONTAL)
scrollbar_horizontal.pack(side="bottom",fill="x")

text.pack(fill="both",expand=True)
ventana.mainloop()