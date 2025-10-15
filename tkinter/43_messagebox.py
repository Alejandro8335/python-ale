from tkinter import messagebox,Tk

# ℹ️ messagebox.showinfo() → para mostrar información

# ⚠️ messagebox.showwarning() → para advertencias

# ❌ messagebox.showerror() → para errores

# ✅ messagebox.askyesno() → para preguntas con respuesta sí/no

# ❓ messagebox.askquestion() → para preguntas generales


ventana = Tk()

respuesta = messagebox.askyesno("¿Salir?", "¿Estás seguro que querés cerrar el bloc de notas?")
#devuelve True o False
if respuesta:
    ventana.destroy()
    
ventana.mainloop()
