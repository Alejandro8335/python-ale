import tkinter as tk
import socket

#objeto tk
ventana = tk.Tk()
ventana.title("on/off")

ESP32_IP = "192.168.100.219"
ESP32_PORT = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

label_esp32 = tk.Label(ventana,text="disconnect")
label_esp32.grid(row=1,column=1,padx=5,pady=5)

#estado
client = None
on_off = False
connect = False

def Connect():
    global client,connect,client_socket
    try:
        if not client:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client = True
        if not connect:
            client_socket.connect((ESP32_IP, ESP32_PORT))
            label_esp32.config(text="connect")
            connect = True
        
        
    except Exception as e:
        print(e)

def On_off():
    global on_off,connect
    # Intentar conectar si aún no lo estamos
    if not connect:
        Connect()
        if not connect:
            return

    try:
        mensaje = "1" if not on_off else "2"
        client_socket.send(mensaje.encode())

        answer = client_socket.recv(64).decode().strip()
        if answer == "1":
            button.config(text="On")
            on_off = True
        elif answer == "2":
            button.config(text="Off")
            on_off = False
        print(answer)
    except Exception as e:
        print("Send error:", e)

def Disconnect():
    global on_off ,connect,client
    try:
        if connect:
            if on_off:
                On_off()
            client_socket.send("3".encode())
            msg = client_socket.recv(64).decode().strip()
            if  msg == "3":
                label_esp32.config(text="disconnect")
                print(msg)
                connect = False 
                client = False
            client_socket.close()
    except Exception as e:
        print(e)
        
        
connect_button = tk.Button(ventana,text="connect",command=Connect)
disconnect_button = tk.Button(ventana,text="disconnect",command=Disconnect)

connect_button.grid(row=0,column=0,padx=5,pady=5)
disconnect_button.grid(row=0,column=1,padx=5,pady=5)

button = tk.Button(ventana,text="on/off",command=On_off)
button.grid(row=1,column=0,padx=5,pady=5)

ventana.mainloop()