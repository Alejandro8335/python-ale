import tkinter as tk

#mause button
def on_click(event):
    print("pressed")
    
ventana = tk.Tk()

button = tk.Button(ventana,text="tap")
button.pack()

button.bind("<Button-2>", on_click)

#teclado
button2 = tk.Button(ventana,text="w")
button2.pack()

def on_key(event):
    if event.char == "w":
        print("w")
    
button2.bind("<KeyPress>",on_key)
ventana.bind("<KeyPress>",on_key)

#configurar ventana
def on_resize(event):
    print(f"ventana nueva:{event.width}*{event.height}")

ventana.bind("<Configure>",on_resize)

#mause move

def mause_move(event):
    print(f"x= {event.x}/y= {event.y}")
    
ventana.bind("<Motion>",mause_move)

ventana.mainloop()