import socket
import ast
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setblocking(False)
#AF_INET significa IPv4 (direcciones como 192.168.0.10)
#SOCK_STREAM → conexión orientada a flujo, usa TCP (confiable, ordenado, orientado a conexión).

ESP32_IP = "192.168.100.219"
ESP32_PORT = 8080

connect = False
client = False
def Connect():
    global connect, client_socket, client
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(5)  # evita bloqueos largos
        client_socket.connect((ESP32_IP, ESP32_PORT))
        print("connect")
        connect = True
        client = True
    except socket.timeout:
        print("Tiempo de conexión agotado")
        connect = False
        client = False
    except Exception as e:
        print(f"Error: {e}")
        connect = False
        client = False
        
buffer = ""      
def Input_esp():
    global buffer, connect, client_socket
    if connect and client_socket:
        try:
            data = client_socket.recv(64)
            if data:
                buffer += data.decode()
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    if line.strip():
                        tupla = ast.literal_eval(line)
                        print("Recibido:", tupla)
        except TimeoutError:
            # No llegaron datos en el tiempo límite, seguimos sin error
            pass
        except Exception as e:
            print(f"Error de recepción: {e}")
            connect = False
while True:
    Connect()
    input()