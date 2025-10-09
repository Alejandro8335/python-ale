# faltan 3 funciones(parentesis,puntos decimal y que se ponga comas separadores de miles)

# con los parentesis vamos a tener que hacer algo para que eval los interprete "8(5)"
# como multiplicacion y no de error

# tenemos problemas con los puntos decimales, si pongo 3.5.6 da error

# tenemos problemas con los negativos pq no me deja ponerlos al principio y tmp detras de la mul y div,

# tenemos que hacer que se sustituyan los operadores si se ponen dos seguidos

# podemos poner dos bottones para movernos a izq y der

import tkinter as tk

ventana = tk.Tk()

# funcion de operaciones
def calcular():
    global entry
    try:
        resultado = eval(entry.get())# e interpreta el contenido de la cadena como si fuera código Python y lo ejecuta en tiempo real.
        entry.delete(0, tk.END)
        if resultado % 1 == 0:
            entry.insert(0, int(resultado))  # Mostrar como entero si no hay parte decimal
        else:
            entry.insert(0, resultado)  # Mostrar como float si hay parte decimal
    
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, e)

def operaciones(signo):
    global entry
    if entry.get() and entry.get()[-1] not in "+-*/%.":  # Evita operadores consecutivos
        entry.insert(tk.END, str(signo))

# funciones de limpieza
def clear():
    global entry
    entry.delete(0, tk.END) 
    
def borrar():
    global entry
    entry.delete(len(entry.get())-1, tk.END)

# funciones de numeros

def agregar_numero(num):
    global entry
    entry.insert(tk.END, str(num))

# pantalla 
entry = tk.Entry(ventana,width=8,font=("Arial",24),bd=6,relief="ridge",justify="right")
entry.grid(row=0, column=0, columnspan=4)

# buttons

# linea 1
button_clear = tk.Button(ventana, text="AC",width=4,height=2,command=lambda:clear())
button_clear.grid(row=1, column=0)

button_parentesis = tk.Button(ventana, text="(  )",width=4,height=2)
button_parentesis.grid(row=1, column=1)

button_porcentaje = tk.Button(ventana, text="%",width=4,height=2,command=lambda:operaciones("%"))
button_porcentaje.grid(row=1, column=2)

button_dividir = tk.Button(ventana, text="/",width=4,height=2,command=lambda:operaciones("/"))
button_dividir.grid(row=1, column=3)

# linea 2
button_7 = tk.Button(ventana, text="7",width=4,height=2,command=lambda:agregar_numero(7))
button_7.grid(row=2, column=0)

button_8 = tk.Button(ventana, text="8",width=4,height=2,command=lambda:agregar_numero(8))
button_8.grid(row=2, column=1)

button_9 = tk.Button(ventana, text="9",width=4,height=2,command=lambda:agregar_numero(9))
button_9.grid(row=2, column=2)

button_multiplicar = tk.Button(ventana, text="*",width=4,height=2,command=lambda:operaciones("*"))
button_multiplicar.grid(row=2, column=3)

# linea 3
button_4 = tk.Button(ventana, text="4",width=4,height=2,command=lambda:agregar_numero(4))
button_4.grid(row=3, column=0)

button_5 = tk.Button(ventana, text="5",width=4,height=2,command=lambda:agregar_numero(5))
button_5.grid(row=3, column=1)

button_6 = tk.Button(ventana, text="6",width=4,height=2,command=lambda:agregar_numero(6))
button_6.grid(row=3, column=2)

button_restar = tk.Button(ventana, text="-",width=4,height=2,command=lambda:operaciones("-"))
button_restar.grid(row=3, column=3)

# linea 4
button_1 = tk.Button(ventana, text="1",width=4,height=2,command=lambda:agregar_numero(1))
button_1.grid(row=4, column=0)

button_2 = tk.Button(ventana, text="2",width=4,height=2,command=lambda:agregar_numero(2))
button_2.grid(row=4, column=1)

button_3 = tk.Button(ventana, text="3",width=4,height=2,command=lambda:agregar_numero(3))
button_3.grid(row=4, column=2)

button_sumar = tk.Button(ventana, text="+",width=4,height=2,command=lambda:operaciones("+"))
button_sumar.grid(row=4, column=3)

# linea 5
button_0 = tk.Button(ventana, text="0",width=4,height=2,command=lambda:agregar_numero(0))
button_0.grid(row=5, column=1)

button_float = tk.Button(ventana, text=".",width=4,height=2)# hay que crear un funcion que evite poner mas de un punto
button_float.grid(row=5, column=0)

button_borrar = tk.Button(ventana, text="⌫",width=4,height=2,command=lambda:borrar())
button_borrar.grid(row=5, column=2)

button_igual = tk.Button(ventana, text="=",width=4,height=2,command= calcular)
button_igual.grid(row=5, column=3)

ventana.mainloop()