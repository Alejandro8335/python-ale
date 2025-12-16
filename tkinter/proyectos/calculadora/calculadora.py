import re
import tkinter as tk

# funcion de operaciones
def calcular():
    global entry, label
    try:
        contenido = entry.get()
        # cierra los parentesis abiertos
        falta_parentesis = contenido.count("(") - contenido.count(")")
        if falta_parentesis > 0:
            contenido += ")"*falta_parentesis
        else:
            contenido = "("*(falta_parentesis*-1) + contenido
        #label de expresion anterior
        label.config(text=contenido)

        # poniendo * entre parentesis y numeros
        for i in reversed(list(re.finditer(r"(\d+|\))\(", contenido))):# devuelve objetos Match
            pos = i.start() + len(i.group(1))# devuelve un número entero
            # i.start() → posición numérica donde empieza la coincidencia.
            # i.end() → posición numérica donde termina (no inclusiva).
            # i.group() → el texto que coincide.
            #.group(1) devuelve solo lo que está dentro del primer grupo de paréntesis del patrón
            contenido = contenido[:pos] + "*" + contenido[pos:]

        # i.start() → devuelve la posición inicial donde se encontró el patrón.

        # contenido[:i.start()]	Devuelve la parte antes del patrón
        # contenido[i.start():]	Devuelve la parte desde el patrón
        # i.start()	Devuelve la posición numérica


        # \d+
        # \d → cualquier dígito (0–9)

        # + → uno o más del elemento anterior (dígitos en este caso)

        # | → "o"
        # \) → un paréntesis de cierre literal
        # (\d+|\)) → grupo que puede ser un número o un )
        # \( → un paréntesis de apertura literal

        # busca parentecis de ) seguidos de numeros
        for i in reversed(list(re.finditer(r"\)\d+", contenido))):
            pos = i.start() + 1
            contenido = contenido[:pos] + "*" + contenido[pos:]


        # porcentajes
        for i in reversed(list(re.finditer(r"(\d+|\))%", contenido))):
            pos = i.start() + len(i.group(1))
            contenido = contenido[:pos] + "/100*" + contenido[pos+1:]#con + 1 me desplazo un caracter para eliminarlo (%)
            # % = /100 se pone al final de la expresion

        # print para debuguear
        # print(contenido)
        
        resultado = eval(contenido)# interpreta el contenido de la cadena como si fuera código Python y lo ejecuta en tiempo real.
        entry.delete(0, tk.END)
        if resultado % 1 == 0:
            entry.insert(0, int(resultado))  # Mostrar como entero si no hay parte decimal
        else:
            entry.insert(0, resultado)  # Mostrar como float si hay parte decimal

    except ZeroDivisionError:
        label.config(text="ZeroDivisionError")

    except Exception as excep:
        label.config(text=excep)

def operaciones(signo):
    global entry
    str_ = entry.get()
    if (signo == "+")and str_ and (str_[-1] == "-"): # saca el signo - si se pone +
        entry.delete(len(str_)-1, tk.END)
            
    elif str_:
        match str_:
            case x if (x[-1] in "+-*/%.("):  # Evita operadores consecutivos
                if len(x) > 1 and not (x[-2] in "+-*/%."):
                    entry.delete(len(x)-1, tk.END)
                    entry.insert(tk.END, signo)

            case _: # Caso general
                entry.insert(tk.END, signo)
                
def sustraccion():
    global entry
    # Permite el signo negativo al inicio pero evalua que no se repitan los signos -
    match entry.get():
        case x if x and x[-1] == "+":
            entry.delete(len(x)-1,tk.END)
            entry.insert(tk.END, "-")
        case x if x == "" or x[-1] != "-":
            entry.insert(tk.END, "-")

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

# funciones de puntos decimales

def agregar_punto():
    global entry
    str_ = entry.get()

    # Verifica que no termine en operador
    if str_ and str_[-1] not in "+-*/%.()":
        # Toma el último elemento de la lista que se va a dividir por +\-*/%
        ultimo_numero = re.split(r"[+\-*/%]", str_)[-1]
        # verifica que el elemnto no tenga punto
        if "." not in ultimo_numero:
            entry.insert(tk.END, ".")

# funcion de parentesis
def agregar_parentesis():
    global entry
    str_ = entry.get()
    if str_:
        bool_count = str_.count("(") > str_.count(")")
        match str_:
            case x if (x[-1] not in "+-*/%.(") and bool_count:
                entry.insert(tk.END,")")
                
            case x if x[-1] == ".":
                entry.delete(len(x)-1, tk.END)
                if bool_count:
                    entry.insert(tk.END,")")
                else:
                    entry.insert(tk.END,"(")
            case _:
                entry.insert(tk.END,"(")

    else:
        entry.insert(tk.END,"(")

# ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("200x300")

# pantalla de la calculadora
entry = tk.Entry(ventana,width=8,font=("Arial",24),bd=6,relief="ridge",justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# buttons

# del 1 al 9 y 1
for idx , num in enumerate([7,8,9,4,5,6,1,2,3]):
    button = tk.Button(ventana, text=str(num),width=4,height=2,command=lambda n=num:agregar_numero(n))
    button.grid(row= 3 + idx // 3, column= idx % 3 , sticky="nsew")

# botones de operaciones menos el -
for row,column,signo in [(2,2,"%"),(2,3,"/"),(3,3,"*"),(5,3,"+")]:
    button_signo = tk.Button(ventana, text=signo,width=4,height=2,command=lambda signo=signo: operaciones(signo))# no lo toque larga historia
    button_signo.grid(row=row, column=column,sticky="nsew")

# linea 2(btns: clear, parentesis)
# linea 6(btns: 0, ., ⌫, =)
for row,column,signo,func in [(2,0,"AC",lambda:clear()),(2,1,"(  )",lambda:agregar_parentesis()),(6,2,"⌫",lambda:borrar()),(6,3,"=",lambda:calcular()),(6,1,".",lambda:agregar_punto()),(6,0,"0",lambda:agregar_numero(0)),(4,3,"-",lambda: sustraccion())]:
     button_clear = tk.Button(ventana, text=signo,width=4,height=2,command=func)
     button_clear.grid(row=row, column=column,sticky="nsew")

# label de exprecion anterior
label = tk.Label(ventana, width=8, font=("Arial", 10),bd=6,relief="ridge",justify="right",anchor="e")
label.grid(row=1, column=0, columnspan=4, sticky="nsew")

# anchor="e" → alinea el contenido hacia el este (derecha)
# Otros valores posibles: "w" (izquierda), "center", "n", "s", etc

# columnas y filas expansibles
for i in range(7):
    ventana.grid_rowconfigure(i, weight=1)
for j in range(4):
    ventana.grid_columnconfigure(j, weight=1)

ventana.mainloop()