import socket
import ast
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setblocking(False)
#AF_INET significa IPv4 (direcciones como 192.168.0.10)
#SOCK_STREAM → conexión orientada a flujo, usa TCP (confiable, ordenado, orientado a conexión).

ESP32_IP = "192.168.100.219"
ESP32_PORT = 8080

connect = False
client = True
def Connect():
    global connect,client_socket,client
    try:
        if not client:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client = True
        if not connect:
            client_socket.connect((ESP32_IP, ESP32_PORT))
            label_state.config(text="connect")
            connect = True
        
        
    except Exception as e:
        label_error.config(text=e)
        
def Disconnect():
    global connect,client
    try:
        if connect:
            label_state.config(text="disconnect")
            connect = False 
            client = False
            client_socket.close()
    except Exception as e:
        label_error.config(text=e)

def Pack_entry():
    global connect
    if not connect:
        Connect()
    try:
        E_def = int(entry_def.get())
        E_Pin = int(entry_Pin.get())
        E_number = int(entry_number.get())  
        exists_Pin = False
        exists_def = False
        exists_number = True
        for i in [1,3,4,5,12,13,14,16,17,18,19,21,22,23,25,26,27,32,33]:
            if E_Pin == i:
                exists_Pin = True
        if  exists_Pin:
            match E_def:
                case 1:
                    exists_def = True
                    if  not (E_number == 1 or E_number == 0):
                        label_error.config(text="The number you entered is not valid for this function; only the values 1 or 0.")
                        exists_number = False
                case 2:
                    exists_def = True
                    if not (0 <= E_number <= 1023):
                        label_error.config(text="The number you entered is not valid for this function; the PWM value range is from 0 to 1023.")
                        exists_number = False
                case _:
                    label_error.config(text="The function does not exist,1/value or 2/PWM")
            
            if exists_def and exists_number:
                tupla = str(tuple([E_def,E_Pin,E_number]))
                client_socket.send(tupla.encode())
                label_error.config(text="package sent")
                
        else:
            label_error.config(text="The Pin does not exist")
            
    except Exception as e:
        label_error.config(text=e)
        
buffer = ""
def Input_esp():
    global buffer,connect
    if connect:
        try:
            data = client_socket.recv(64).decode()
            objeto, numero = data
            buffer += data
            # Mientras haya líneas completas en buffer…
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                if not line:
                    continue
                try:
                    objeto, numero = ast.literal_eval(line)
                    # Aquí procesás `objeto` y `numero`
                    print("Recibí:", objeto, numero)
                except Exception as e:
                    print("Error parseando:", repr(line), e)
        except BlockingIOError:
            # No hay datos en este ciclo, seguimos
            pass

        # vuelvo a llamar tras 50 ms sin bloquear la GUI
        ventana.after(50, Input_esp)
import tkinter as tk

ventana = tk.Tk()
ventana.title("client")

label_state = tk.Label(ventana,text="disconnect")
button_connect = tk.Button(ventana,text="connect",command=Connect)
button_disconnect = tk.Button(ventana,text="disconnect",command=Disconnect)

button_connect.grid(row=0,column=0,padx=5,pady=5)
button_disconnect.grid(row=0,column=1,padx=5,pady=5)
label_state.grid(row=0,column=2,padx=5,pady=5)

entry_def = tk.Entry(ventana)
entry_def.insert(0,"def:1/value,2/PWM")
entry_Pin = tk.Entry(ventana)
entry_Pin.insert(0,"Pin")
entry_number = tk.Entry(ventana)
entry_number.insert(0,"number:PWM(0-1023)")

entry_def.grid(row=1,column=0,padx=5,pady=5)
entry_Pin.grid(row=1,column=1,padx=5,pady=5)
entry_number.grid(row=1,column=2,padx=5,pady=5)

button_send = tk.Button(ventana,text="send",command=Pack_entry)
label_error = tk.Label(ventana,text="There is no error.")

button_send.grid(row=2,column=0,padx=5,pady=5)
label_error.grid(row=2,column=1,padx=5,pady=5)

label_input_button = tk.Label(ventana,text="input button")
label_input_hcsr04 = tk.Label(ventana,text="input hcsr04")

label_input_button.grid(row=3,column=0,padx=5,pady=5)
label_input_hcsr04.grid(row=3,column=1,padx=5,pady=5)

ventana.after(50, Input_esp)
ventana.mainloop()