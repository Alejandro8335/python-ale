import tkinter as tk
import socket

#objeto tk
ventana = tk.Tk()
ventana.title("on/off")

ESP32_IP = "192.168.100.219"
ESP32_PORT = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

label_esp32 = tk.Label(ventana,text="disconnect")
label_esp32.grid(row=1,column=0,padx=5,pady=5)

#estado
client = None
on_off = False
connect = False

def Connect():
    global client,client_socket,connect
    try:
        if not connect:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not connect:
            client_socket.connect((ESP32_IP, ESP32_PORT))
            label_esp32.config(text="connect")
            client = True
            connect = True
        
        
    except Exception as e:
        print(e)

label_on_off = tk.Label(ventana,text="off")
label_on_off.grid(row=2,column=1,padx=5,pady=5)
def On_off():
    global on_off
    # Intentar conectar si aún no lo estamos
    if not connect:
        Connect()
        if not connect:
            return

    try:
        mensaje = "1" if not on_off else "2"
        client_socket.send(mensaje.encode())
        on_off = not on_off
        label_on_off.config(text="On" if on_off else "Off")
    except Exception as e:
        print("Send error:", e)

def Disconnect():
    global client , on_off ,connect
    try:
        label_esp32.config(text="disconnect")
        if on_off:
             On_off()
        client = False
        connect = False
        client_socket.close()
        
    except Exception as e:
        print(e)
        
        
connect_button = tk.Button(ventana,text="connect",command=Connect)
disconnect_button = tk.Button(ventana,text="disconnect",command=Disconnect)

connect_button.grid(row=0,column=0,padx=5,pady=5)
disconnect_button.grid(row=0,column=1,padx=5,pady=5)

button = tk.Button(ventana,text="on/off",command=On_off)
button.grid(row=2,column=0,padx=5,pady=5)

ventana.mainloop()