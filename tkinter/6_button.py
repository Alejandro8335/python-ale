import tkinter as tk

ventana = tk.Tk()
ventana.title("button")

button = tk.Button(ventana,text="tap")
button.configure(width=5,height=1,bg ="#23a2b9",bd=5)
button.pack()

def button_tap():
    print("tap")
    
button.config(command=button_tap)
ventana.mainloop()